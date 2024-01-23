import boto3

def test_run_multiple_instances_in_same_command():
    instance_count = 4
    client = boto3.client("ec2", region_name="ap-south-1")
    client.run_instances(
        ImageId="ami-1234abcd", MinCount=instance_count, MaxCount=instance_count
    )
    reservations = client.describe_instances()["Reservations"]

    reservations[0]["Instances"].should.have.length_of(instance_count)

    instances = reservations[0]["Instances"]
    for i in range(0, instance_count):
        instances[i]["AmiLaunchIndex"].should.be(i)
