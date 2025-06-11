import boto3

# Create an Ec2 instance
def create_ec2_instance():
    try:
        print("Creating EC2 instance")
        ec2 = boto3.client('ec2')
        response = ec2.run_instances(
            ImageId="ami-02457590d33d576c3", #AMI ID for Amazon Linux 2023 in us-east 1 region
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="test-ec2-key-pair")
    except Exception as e:
        print(e)
#create_ec2_instance() this is the function call

#describing an Ec2 instance

def describe_ec2_instance():
    try:
        print("Describing EC2 instance")
        ec2 = boto3.client('ec2')
        response= ec2.describe_instances()
        print(response)
    except Exception as e:
        print(e)
#describe_ec2_instance() this is the function call

#stopping an instance

def get_one_instance_id():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()

    # Loop through reservations and instances
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            return instance['InstanceId']  # Return first instance found

    raise Exception("No instances found.")

def stop_ec2_instance():
    try:
        print("Stopping EC2 instance...")
        instance_id = get_one_instance_id()
        print(f"Stopping instance: {instance_id}")
        ec2 = boto3.client('ec2')
        response = ec2.stop_instances(InstanceIds=[instance_id])
        print(response)
    except Exception as e:
        print(e)

stop_ec2_instance()
