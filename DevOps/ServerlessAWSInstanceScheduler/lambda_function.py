import boto3
import json
from datetime import datetime
import pytz

# AWS Resources
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
ec2 = boto3.client('ec2', region_name='us-east-1')

# DynamoDB Table
TABLE_NAME = "ec2_scheduler"
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    action = event.get("action")
    instance_id = event.get("instance_id")

    if action == "remove_tag":
        return remove_schedule_tag(instance_id)
    
    return check_and_execute_schedules()

def check_and_execute_schedules():
    """ Check EC2 schedules and start/stop instances accordingly. """
    current_time = datetime.utcnow().strftime("%H:%M")
    current_day = datetime.utcnow().strftime("%A").lower()

    response = table.scan()
    for item in response.get("Items", []):
        instance_id = item["instance_id"]
        schedule = item.get("schedule", {})

        if current_day in schedule:
            action = determine_action(schedule[current_day], current_time)
            if action:
                manage_instance(instance_id, action)

    return {"message": "Schedule executed successfully"}

def determine_action(schedule, current_time):
    """ Determine whether to start or stop an instance. """
    if schedule == "stop":
        return "stop"
    
    schedule_parts = schedule.split(", ")
    start_time, stop_time = schedule_parts[0].split(":")[1], schedule_parts[1].split(":")[1]

    if current_time == start_time:
        return "start"
    elif current_time == stop_time:
        return "stop"

    return None

def manage_instance(instance_id, action):
    """ Start or stop an EC2 instance. """
    if action == "start":
        ec2.start_instances(InstanceIds=[instance_id])
        ec2.create_tags(Resources=[instance_id], Tags=[{"Key": "scheduled", "Value": "True"}])
    elif action == "stop":
        ec2.stop_instances(InstanceIds=[instance_id])

def remove_schedule_tag(instance_id):
    """ Remove the schedule tag from an EC2 instance. """
    ec2.delete_tags(Resources=[instance_id], Tags=[{"Key": "scheduled"}])
    return {"message": "Tag removed successfully"}
