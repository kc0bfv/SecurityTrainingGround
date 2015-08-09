#!/usr/bin/env python3

import os.path
import json

from cybersecurity.settings import CONFIG_FILE

requiredInput = [ # Prompt, dictionary key name, default
	("Enter the desired AWS region", "aws_region", "us-east-1"),
	("Enter the desired EC2 availability zone", "aws_avail_zone", "us-east-1a"),
	("Enter your AWS access key", "aws_access_key", ""),
	("Enter your AWS secret key", "aws_secret_key", ""),
	("Enter the EC2 AMI Image ID", "ec2_ami_image_id", ""),
	("Enter the EC2 key name", "ec2_key_name", ""),
	("Enter the desired EC2 instance type", "ec2_instance_type", "t2.medium"),
	("Enter the desired EC2 security group", "ec2_security_group", ""),
	("Enter the desired EC2 subnet ID", "ec2_subnet_id", ""),
	("Enter the AMI's username", "ami_username", ""),
	("Enter the AMI's password", "ami_password", ""),
	("How many hours should images run for", "image_hours", "4"),
	("How many minutes should images run for", "image_minutes", "0"),
	("What's the image's minimum score", "image_scoremin", "0"),
	("What's the image's maximum score", "image_scoremax", "100"),
	("Enter the score server address", "score_server_address", "127.0.0.1"),
	]

def getInput(prompt, key, config, default):
	try:
		internalDefault = config[key]
	except KeyError:
		internalDefault = default
	finally:
		if internalDefault is not "":
			promptDefault = " (" + internalDefault + ")"
		else:
			promptDefault = ""

	prompt = prompt + promptDefault + ": "

	dat = input(prompt)
	if dat is "":
		config[key] = internalDefault
	else:
		config[key] = dat

	return config


# ---------------  MAIN CODE -------------

# Try to read in the existing config
try:
	config = json.load(open(os.path.expanduser(CONFIG_FILE)))
except FileNotFoundError:
	config = dict()

# Read in all the inputs, taking proper defaults into account
for (prompt, key, default) in requiredInput:
	config = getInput(prompt, key, config, default)

# Write out the new config
json.dump(config, open(os.path.expanduser(CONFIG_FILE), "w"))
