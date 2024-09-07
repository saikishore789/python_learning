import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = "eks-terraform-sai"
    response = s3.list_buckets()
    bucket_count = len(response['Buckets'])
    
    print(f"no of s3 buckets: {bucket_count}")
    
    return{
        'statusCode':200,
        'body':{
            'bucket_count': bucket_count
        }
    }