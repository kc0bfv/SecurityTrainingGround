import json
import boto.ec2
import os.path

from SecurityTrainingGround.settings import CONFIG_FILE


def _openConnection(config):
	return boto.ec2.connect_to_region(config["aws_region"],
			aws_access_key_id=config["aws_access_key"],
			aws_secret_access_key=config["aws_secret_key"])

def _listInstances(config, conn):
	# This will list all instances with the subnet_id and security_group, therefore this assumes that you've assigned a subnet_id and security_group pair for only the playground instances...  Don't use those for your other EC2 instances, or they'll get affected by all that touches this...
	reservations = conn.get_all_reservations(
			filters={"subnet-id": config["ec2_subnet_id"],
				"instance.group-id": config["ec2_security_group"]}
			)
	instances = [i for r in reservations for i in r.instances]
	return instances




def readConfig():
	return json.load(open(os.path.expanduser(CONFIG_FILE)))

def listInstances():
	config = readConfig()
	conn = _openConnection(config)
	return [inst.id for inst in _listInstances(config, conn)]

def startInstance(userData=""):
	config = readConfig()
	conn = _openConnection(config)

	reservation = conn.run_instances(config["ec2_ami_image_id"],
			key_name=config["ec2_key_name"],
			instance_type=config["ec2_instance_type"],
			security_group_ids=[config["ec2_security_group"]],
			user_data=userData,
			subnet_id=config["ec2_subnet_id"],
			placement=config["aws_avail_zone"],
			)
	instanceID = reservation.instances[0].id
	return instanceID

def stopInstances(instanceIDs):
	config = readConfig()
	conn = _openConnection(config)

	conn.terminate_instances(instance_ids=instanceIDs)
	
def stopAllInstances():
	config = readConfig()
	conn = _openConnection(config)

	instanceIDs = [i.id for i in _listInstances(config, conn)]
	conn.terminate_instances(instance_ids=instanceIDs)

def getInstIP(instanceID):
	config = readConfig()
	conn = _openConnection(config)

	reservations = conn.get_all_reservations(instance_ids=[instanceID])
	instances = [i for r in reservations for i in r.instances]

	try:
		return instances[0].ip_address
	except IndexError:
		return "0.0.0.0"
