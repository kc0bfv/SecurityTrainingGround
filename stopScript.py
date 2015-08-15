#!/usr/bin/env python3

# Necessary to use the DJANGO database stuff
import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SecurityTrainingGround.settings")

import django
django.setup()


import datetime

from pgmanager.models import EC2Instance

import SecurityTrainingGround.manageEC2 as manageEC2


config = manageEC2.readConfig()


# Find all the instances that are running that aren't assigned a user
allInstances = manageEC2.listInstances()
knownInstances = [inst.instanceID for inst in EC2Instance.objects.all()]
unknownInstances = [inst for inst in allInstances
		if inst not in knownInstances]

print("Instances that do not match those in use by a user:")
print(unknownInstances)


# Which instances in the DB aren't still running?
deadInstances = [inst for inst in knownInstances
		if inst not in allInstances]

print("Instances that are no longer running:")
print(deadInstances)


# Find all the old instances that are still running
timeDelta = datetime.timedelta(hours=int(config["image_hours"]),
		minutes=int(config["image_minutes"]))
curTime = datetime.datetime.now(datetime.timezone.utc)
oldInstances = [inst.instanceID
		for inst in EC2Instance.objects.all()
		if ((curTime - inst.startTime) > timeDelta)]


print("Old instances:")
print(oldInstances)

allToStop = oldInstances + unknownInstances + deadInstances
# Stop all of them
if allToStop:
	manageEC2.stopInstances(allToStop)

# Remove their DB entries
for instID in allToStop:
	for inst in EC2Instance.objects.filter(instanceID=instID):
		inst.delete()

