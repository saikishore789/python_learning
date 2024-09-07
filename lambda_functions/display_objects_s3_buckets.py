import os
import boto3

os.environ['input_bucket'] = 'eks-terraform-sai'

s3_client = boto3.client("s3") # Importing s3 client 

def lambda_handler(event,context):
    
    print("Loading the function...")

    response = s3_client.list_objects_v2(Bucket=os.environ['input_bucket'])
    s3_bucket = os.environ['input_bucket']
    json_file = response['Contents'][2]['Key']
    print(s3_bucket)
    print(json_file)