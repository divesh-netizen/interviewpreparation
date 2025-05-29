from flask import Flask, request, jsonify
import boto3
import uuid

app = Flask(__name__)

# AWS Resources
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
lambda_client = boto3.client('lambda', region_name='us-east-1')

# DynamoDB Table Name
TABLE_NAME = "ec2_scheduler"
table = dynamodb.Table(TABLE_NAME)

# Lambda Function Name
LAMBDA_FUNCTION = "ec2_instance_scheduler"

@app.route('/schedule', methods=['POST'])
def create_schedule():
    """ Create a new EC2 instance schedule. """
    data = request.json
    instance_id = data.get("instance_id")
    schedule = data.get("schedule")

    if not instance_id or not schedule:
        return jsonify({"error": "Missing instance_id or schedule"}), 400

    schedule_id = str(uuid.uuid4())

    table.put_item(
        Item={
            "instance_id": instance_id,
            "schedule_id": schedule_id,
            "schedule": schedule
        }
    )

    return jsonify({"message": "Schedule created successfully", "schedule_id": schedule_id})

@app.route('/schedule/<instance_id>', methods=['GET'])
def get_schedule(instance_id):
    """ Retrieve a schedule for a specific EC2 instance. """
    response = table.get_item(Key={"instance_id": instance_id})
    if "Item" not in response:
        return jsonify({"error": "Schedule not found"}), 404

    return jsonify(response["Item"])

@app.route('/schedule/<instance_id>', methods=['PUT'])
def update_schedule(instance_id):
    """ Update the schedule of an EC2 instance. """
    data = request.json
    new_schedule = data.get("schedule")

    if not new_schedule:
        return jsonify({"error": "Missing schedule"}), 400

    response = table.update_item(
        Key={"instance_id": instance_id},
        UpdateExpression="SET schedule = :s",
        ExpressionAttributeValues={":s": new_schedule},
        ReturnValues="UPDATED_NEW"
    )

    return jsonify({"message": "Schedule updated", "updated_schedule": response["Attributes"]["schedule"]})

@app.route('/schedule/<instance_id>', methods=['DELETE'])
def delete_schedule(instance_id):
    """ Delete a schedule and remove the tag from EC2 instance. """
    table.delete_item(Key={"instance_id": instance_id})

    # Invoke Lambda to remove tag
    lambda_client.invoke(
        FunctionName=LAMBDA_FUNCTION,
        InvocationType="Event",
        Payload=f'{{"action": "remove_tag", "instance_id": "{instance_id}"}}'
    )

    return jsonify({"message": "Schedule deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
