spam = {
			'title':"Spam Email",
			'shortname':"spam",
			'lessonContentFile':"content/spamEmail.html",
			'questions':[
				{
					'question':"What is spam email?",
					'pointValue':1,
					'answers':[
						{
							'answer':"Email that&apos;s about a delicious pork product",
							}, # Answer end
						{
							'answer':"Junk email, email that you don&apos;t want, email from a company that you don&apos;t already buy stuff from that&apos;s trying to sell you something",
							'correct':True,
							}, # Answer end
						{
							'answer':"Email from a company that you normally buy stuff from",
							}, # Answer end
						{
							'answer':"Email that&apos;s not kosher",
							}, # Answer end
						], # End of answers
					}, # Question end
				{
					'question':"Do legitimate products ever advertise using spam?",
					'pointValue':1,
					'answers':[
						{
							'answer':"Sometimes",
							}, # Answer end
						{
							'answer':"Oh yeah!  All the best products are advertised using spam!",
							}, # Answer end
						{
							'answer':"Rarely",
							}, # Answer end
						{
							'answer':"No",
							'correct':True,
							}, # Answer end
						], # End of answers
					}, # Question end
				{
					'question':"Does spam ever fool people?",
					'pointValue':1,
					'answers':[
						{
							'answer':"Only stupid people",
							}, # Answer end
						{
							'answer':"All the time - those hackers are tricky, and skilled, and like to play on human weakness",
							'correct':True,
							}, # Answer end
						{
							'answer':"Never!  Hackers cannot make email that looks like it comes from Amazon, or Paypal, or other legitimate companies.",
							}, # Answer end
						{
							'answer':"Only careless people",
							}, # Answer end
						], # End of answers
					}, # Question end
				{
					'question':"What is phishing?",
					'pointValue':1,
					'answers':[
						{
							'answer':"It&apos;s when you go looking for fish in Minecraft.",
							}, # Answer end
						{
							'answer':"It&apos;s the computer equivalent of going fishing on a lake.",
							}, # Answer end
						{
							'answer':"When an email hooks processes on your computer",
							}, # Answer end
						{
							'answer':"Email that tries to trick you into revealing your personal information, like passwords or account numbers, through fake webpages.",
							'correct':True,
							}, # Answer end
						], # End of answers
					}, # Question end
				{
					'question':"How can you recognize spam?",
					'pointValue':1,
					'answers':[
						{
							'answer':"Spam often has strange-looking URLs, may try to sell you something, and often has spelling errors",
							'correct':True,
							}, # Answer end
						{
							'answer':"It comes from your friends",
							}, # Answer end
						{
							'answer':"It tastes delicious fried, with eggs",
							}, # Answer end
						{
							'answer':"It&apos;s always easy to recognize spam because Google and Yahoo always separate it from the rest of your email",
							}, # Answer end
						], # End of answers
					}, # Question end
				{
					'question':"What should you do with spam?",
					'pointValue':1,
					'answers':[
						{
							'answer':"Consider purchasing the things it advertises",
							}, # Answer end
						{
							'answer':"Send it to your friends",
							}, # Answer end
						{
							'answer':"Delete it, and don't click on links",
							'correct':True,
							}, # Answer end
						{
							'answer':"Try to click on the links inside to see what it&apos;s about",
							}, # Answer end
						], # End of answers
					}, # Question end
				{
					'question':"Which of the following is most likely a fake link?",
					'pointValue':1,
					'answers':[
						{
							'answer':"<a href=\"http://www.amazon.com/\" target=\"_blank\" onClick=\"return false;\">Login to Amazon</a>",
							}, # Answer end
						{
							'answer':"<a href=\"http://www.facebook.real.cn\" target=\"_blank\" onClick=\"return false;\">Login to Facebook</a>",
							'correct':True,
							}, # Answer end
						{
							'answer':"<a href=\"http://www.google.com/\" target=\"_blank\" onClick=\"return false;\">Login to Google</a>",
							}, # Answer end
						{
							'answer':"<a href=\"https://signin.ebay.com/\" target=\"_blank\" onClick=\"return false;\">Login to eBay!</a>",
							}, # Answer end
						], # End of answers
					}, # Question end
				{
					'question':"Which of the following is most likely a real email, and not spam?",
					'pointValue':1,
					'answers':[
						{
							'answer':"""If you own a travel related website, why not submit your site to our directory.
							<br><br>Just select the appropriate category and subcategory and enter your title and description.
							<br><br>Click here to start: <a href="http://www.holasdfa-travel-directory.com" target="_blank" onClick="return false;">http://www.holasdfa-travel-directory.com</a>
							<br><br>This footnote confirms that this email message has been swept by Anti Virus Software for the presence of computer viruses.""",
							}, # Answer end
						{
							'answer':"""Hello
							<br><br><a href="www.Selasdff-catering-breaks.com" target="_blank" onClick="return false;">www.Selasdff-catering-breaks.com"</a> is now becoming one of the largest sites on the internet for people who wish to list their own properties.
							<br><br>We already have 1000's of properties listed but want to make sure you already have listed your properties.
							<br><br>So please feel free to add your property or properties.""",
							}, # Answer end
						{
							'answer':"""Hello again
							<br><br><a href="http://Selfasdf-catering.co.uk" target="_blank" onClick="return false;">Selfasdf-catering.co.uk</a> was recently launched and if you have not yet added your property for free then please do as we have had many properties added in the past few days.
							<br><br>Firstly register at:
							<br><a href="http://www.selfasdf-catering.co.uk/register/" target="_blank" onClick="return false;">http://www.selfasdf-catering.co.uk/register/</a>
							<br><br>and you will be emailed an authorisation key.
							<br><br>Thanks for your time and please pass this email onto anyone you think may be interested to list for free.
							<br><br>Benji
							<br><a href="http://www.selfasdf-catering.co.uk" target="_blank" onClick="return false;">www.selfasdf-catering.co.uk</a>""",
							}, # Answer end
						{
							'answer':"""IMPORTANT: PASSWORD UPDATE
							<br><br>Dear eBay Member,
							<br>To help ensure customers' trust and security on eBay, I am asking all eBay users to change their passwords.
							<br>Here's why: Recently, our company discovered a cyberattack on our corporate information network. This attack compromised a database containing eBay user passwords.
							<br>What's important for you to know: We have no evidence that your financial information was accessed or compromised. And your password was encrypted.
							<br><a href="http://announcements.ebay.com/2014/05/important-please-change-your-ebay-password/" target="_blank" onClick="return false;">Read full eBay Announcement</a>""",
							'correct':True,
							}, # Answer end
						], # End of answers
					}, # Question end
				{
					'question':"Which of the following is most likely a real email, assuming that you actually use Yahoo, CPS Energy, and USAA?",
					'pointValue':1,
					'answers':[
						{
							'answer':"""<h2>From: Yahoo! Inc. Microsoft Corp. (lynreim@mweb.co.za)</h2>
							<br><br>Congratulations!  You won the Yahoo! Microsoft Corp. email sweepstakes!  <a href="http://yaho0.cn/winning.pdf13.pdf" target="_blank" onClick="return false;">YAHOO_MSN WINNING NOTIFICATION.pdf</a>
							<br><br><a href="http://yaho0.cn/winning.pdf13.pdf" target="_blank" onClick="return false;">View online</a>
							<br><br><a href="http://yaho0.cn/winning.pdf13.pdf" target="_blank" onClick="return false;">Download as zip</a>
							<br><br>Email Subscriber, view attached PDF for winning information""",
							}, # Answer end
						{
							'answer':"""<h2>From: CPS Energy Billing System (DoNotReply@izakikensetsu.sakura.ne.jp)</h2>
							<br><br>Your latest CPS Energy bill is now available to view online.
							<br><br>Account Number : 476038593
							<br>Bill date: 02/12/2014
							<br>Total Amount Due: $524.30
							<br><br>To view your most recent bill, please <a href="http://www.cpxenergy.com/bill476038593/" target="_blank" onClick="return false;">click here</a>. You must log-in to your account or register for an online account to view your statement.
							<br><br>There are many options to pay your bill. Sign up for the Automatic Payment Plan to have your payment automatically deducted from your bank or credit card. Pay electronically online at the Account Center, visit an Authorized Payment Center or send a check by mail.
							<br><br>Our monthly bill inserts you energy-saving tips, regulatory updates and more.
							<br><br>EMAIL ADDRESS RESPONSIBILITY
							<br>To ensure timely receipt of your bill and other communications, copy this e-mail address into your approved mailing list, so it is not blocked by your protection software.""",
							}, # Answer end
						{
							'answer':"""<h2>From: USAA (USAA.Web.Services@customermail.usaa.com)</h2>
							<br><br>Dear USAA customer,
							<br>You have the following new documents on <a href="http://usaa.com/" target="_blank" onClick="return false;">http://usaa.com</a>. Log on to view your documents.
							<br><br>SAVINGS ******4321 DEC 2012 STATEMENT
							<br><br>If you don't want to receive this e-mail notification when your new documents are posted to usaa.com, you can change your preferences.""",
							'correct':True,
							}, # Answer end
						{
							'answer':"""<h2>From: Mrs.Sandra Sify (jp@eukor.com)</h2>
							<br><br>FROM THE DESK OF
							<br>MRS SANDRA SIFY
							<br>ABUJA-NIGERIA
							<br><br>My Dear Beneficiary
							<br>Very Important Information Regarding Your Outstanding Funds.
							<br>I write to enquire from you if you have received your outstanding funds till now which the answer is NO. You have been under the cage of greedy and non authentic officials who has been deceiving you for a long time in the guise of releasing your funds which they do not have any authority to effect but rather than open up and let you know that they lack the capacity to release your funds, They decided to deceive you till now.
							<br>I have communicated you long time ago and informed you that I am the only person in charge of your funds and I am the only person that can release your funds but it seems that you do not want to believe me due to the fact that you are under the cage and control of those unscrupulous elements/Unauthorized persons who has been deceiving you and requesting for one payment or the other from you till now when you are not required to pay any money to get your funds released to you.
							<br>Infact if you want to receive your outstanding funds immediately, Kindly back to me via return mail to enable me give you details. You must keep this mail confidential until your fund is release to you.
							<br>I will give you further details as soon as i hear from you.
							<br>Your urgent attention is highly imperative.
							<br><br>Yours Faithfully,
							<br><br>Mrs. Sandra Sify
							<br>Assistant Secretary to the consultant Office of Presidency""",
							}, # Answer end
						], # End of answers
					}, # Question end
				{
					'question':"What's a safe way to get to a company's website?",
					'pointValue':1,
					'answers':[
						{
							'answer':"Open a new browser window and type in the address that you already know",
							'correct':True,
							}, # Answer end
						{
							'answer':"Use the link provided in an email",
							}, # Answer end
						{
							'answer':"Look at the address at the bottom of the screen, when you hover over a link, and type that in",
							}, # Answer end
						{
							'answer':"If someone that says they&apos;re from a company calls you, you can use the address they give you",
							}, # Answer end
						], # End of answers
					}, # Question end
				], # End of questions
} # Quiz End
