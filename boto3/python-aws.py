import boto3

ec2 = boto3.client('ec2')

instance_response = ec2.describe_instances(Filters=[{'Name': 'instance-type', 'Values': ['t2.micro']}])

for reservation in instance_response['Reservations']:
    for instance in reservation['Instances']:
        for key, value in instance.items():
            print(key, ':', value)
       

