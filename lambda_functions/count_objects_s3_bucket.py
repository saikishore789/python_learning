import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = "eks-terraform-sai"
    object_count = 0
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            object_count = len(response['Contents'])
         
        # handle pagination if there are more than 1000 objects
        # while response.get('IsTruncated'): # when True, there are more objects to retrieve
        #    continuation_key = response['NextContinuationToken']
        #    response = s3.list_objects_v2(Bucket=bucket_name, ContinuationToken=continuation_key)
        #    object_count += len(response['Contents'])
        
        return{
            'statusCode':200,
            'body':f'Total objects in the bucket {bucket_name}: {object_count}'
        }
    except Exception as e:
         return{
            'statusCode':500,
            'body': f'Error occured: {str(e)}'
        }