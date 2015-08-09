# Constants!  Things to change depending on your image...

# The score breakdown, how many points each section is worth.  Doesn't have to add to 100
$scoreBreakdown = @{"users"=20; "files"=10; "passwords"=20; "firewall"=10; "updates"=10; "shares"=10; "backdoors"=20 }

# The bad users that should get removed
$BADUSERSCONST = @("badGirl", "badGuy")

# The good users that must remain
$GOODUSERSCONST = @("john1965", "franny123", "jeff273", "Administrator", "Guest")

# The files that should get removed, perhaps through uninstalling a program
$badFiles = @("C:\Program Files (x86)\Kazaa Lite\khancer.exe",
    "C:\Users\Administrator\AppData\Local\Obrona Block Ads\ObronaBlockAds.exe",
    "C:\Users\Administrator\AppData\Local\Linkey\Helper.dll",
    "C:\Users\Administrator\AppData\Roaming\uTorrent\uTorrent.exe")

# The maximum password age allowed - anything less than or equal to this is ok
$MAXPWAGECONST = 90

# The minimum password length allowed - anything greater than or equal to this is ok
$MINPWLENCONST = 8

# Shares that should get disabled, note that dollar signs should be escaped with a \ and those shares in single quotes
$BADSHARES = @('\$administratorShare')

# Service Display Names that should get disabled/deleted - maybe because they're backdoors
$BADSERVICECONST = @("Software Update Manager")

# Scheduled Task names that should get disabled/deleted - maybe because they're backdoors
$BADTASKSCONST = @("Microsoft Office Updater")



# Get the score server and user ID
# Uncomment for deployment
$userdata = (Invoke-WebRequest -Uri "http://169.254.169.254/latest/user-data").Content
# For testing only:
#$userdata = "10.0.2.2:8000;1"

# Breakout the data
($serverIP, $userID) = $userdata.Split(";")


# This section looks at users added or deleted
$badUsers = New-Object System.Collections.ArrayList
$goodUsers = New-Object System.Collections.ArrayList
$unkUsers = New-Object System.Collections.ArrayList

$badUsers.AddRange($BADUSERSCONST)
$numBadUsers = $badUsers.Count
$goodUsers.AddRange($GOODUSERSCONST)

Get-WmiObject -Query "Select * from Win32_UserAccount" | foreach {
    if ( $badUsers.Contains($_.Name) -or $goodUsers.Contains($_.Name) ) {
        $len = $badUsers.Remove($_.Name)
        $len = $goodUsers.Remove($_.Name)
    } else {
        $len = $unkUsers.Add($_.Name)
    }
}

$badUsersEliminated = $badUsers.Count                    # Bad users eliminated are good
$goodUsersEliminated = $goodUsers.Count                  # Good users left over are not present on the system, it's bad
$unknownUsersAdded = $unkUsers.Count                     # Unknown users should not be added, it's bad

$goodUserActionsTaken = $badUsersEliminated - $goodUsersEliminated - $unknownUsersAdded
if ($goodUserActionsTaken -lt 0) { $goodUserActionsTaken = 0 }

$userActionsPossible = $numBadUsers
$percentUserActionsScore = $goodUserActionsTaken/$userActionsPossible



# This section looks at files deleted - it's a proxy for programs uninstalled
$badFilesExisting = ($badFiles | where { Test-Path $_ } | measure).Count
$badFilesDeleted = $badFiles.Count - $badFilesExisting

$percentFileActionsScore = $badFilesDeleted / $badFiles.Count


# Check the password policy
$pwPolicy = net accounts
try {
    $maxPwAge = [int32] ($pwPolicy | where { $_ -match "^Maximum password age" } | foreach { $_ -replace ".* ([0-9]+)",'$1'})
} catch {
    $maxPwAge = 200000
}
try {
    $minPwLen = [int32] ($pwPolicy | where { $_ -match "^Minimum password len" } | foreach { $_ -replace ".* ([0-9]+)",'$1'})
} catch {
    $minPwLen = 0
}

$pwPolicyCorrect = ($maxPwAge -le $MAXPWAGECONST) + ($minPwLen -ge $MINPWLENCONST)
$percentPasswordActionsScore = $pwPolicyCorrect / 2


# See if the firewall is enabled
$fwEnabled = if ( (Get-NetFirewallProfile -name (Get-NetConnectionProfile).NetworkCategory).Enabled ) { 1 } else { 0 }
$percentFirewallActionsScore = $fwEnabled / 1


# See if automatic updates are enabled
$autoUpdateEnabled = (New-Object -ComObject "Microsoft.Update.AutoUpdate").Settings.NotificationLevel -eq 4
$percentUpdatesActionsScore = $autoUpdateEnabled / 1



# See if specific shares are still enabled
$netShare = net share
$numSharesEnabled = ($BADSHARES | where { $netShare -match $_ } | measure).Count
$percentShareActionsScore = ($BADSHARES.Count - $numSharesEnabled) / $BADSHARES.Count



# See if the backdoor services are disabled
# For testing...
#$BADSERVICECONST = @("Windows Licensing Monitoring Service", "Routing and Remote Access", "Secure Update", "Microsoft Keyboard Filter")

$badServices = New-Object System.Collections.ArrayList
$allServiceDN = New-Object System.Collections.ArrayList
$badServices.AddRange($BADSERVICECONST)
$allServiceDN.AddRange( (Get-Service | foreach { $_.DisplayName } ) )

$badServiceDisabledCount = (Get-Service | where { ($badServices.Contains($_.DisplayName)) -and
        ($_.Status -ne "Running") -and
        ((Get-WmiObject -Query ("Select StartMode from Win32_Service where Name='" + $_.Name + "'")).StartMode -eq "Disabled"  ) } |
        measure ).Count

$badServiceRemovedCount = ($BADSERVICECONST | where { -not $allServiceDN.Contains( $_ ) } | measure).Count

$badServiceFixedCount = $badServiceDisabledCount + $badServiceRemovedCount




# See if the backdoor scheduled tasks are removed
$badTasks = New-Object System.Collections.ArrayList
$allTasksTN = New-Object System.Collections.ArrayList
$badTasks.AddRange($BADTASKSCONST)
$allTasksTN.AddRange( (Get-ScheduledTask | foreach { $_.TaskName } ) )

$badTaskDisabledCount = (Get-ScheduledTask | where { ($badTasks.Contains($_.TaskName)) -and ($_.State -eq "Disabled")} | measure).Count

$badTaskRemovedCount = ($BADTASKSCONST | where { -not $allTasksTN.Contains( $_ ) } | measure).Count

$badTaskFixedCount = $badTaskDisabledCount + $badTaskRemovedCount


# Combine Backdoor Stats
$backdoorsFixed = $badTaskFixedCount + $badServiceFixedCount
$backdoorsPresent = $BADTASKSCONST.Count + $BADSERVICECONST.Count
$percentBackdoorActionsScore = $backdoorsFixed / $backdoorsPresent



# Calculate the score
$score = ($percentUserActionsScore * $scoreBreakdown["users"]) +
        ($percentFileActionsScore * $scoreBreakdown["files"]) +
        ($percentPasswordActionsScore * $scoreBreakdown["passwords"]) +
        ($percentFirewallActionsScore * $scoreBreakdown["firewall"]) +
        ($percentUpdatesActionsScore * $scoreBreakdown["updates"]) +
        ($percentShareActionsScore * $scoreBreakdown["shares"]) +
        ($percentBackdoorActionsScore * $scoreBreakdown["backdoors"])


$score = [int32] $score


# Send the score
$postParams = @{userID = $userID; score = $score}
$output = Invoke-WebRequest -Uri ("http://" + $serverIP + "/pgmanager/registerScore/") -Method Post -Body $postParams