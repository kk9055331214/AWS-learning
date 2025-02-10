import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    source_bucket = 'my-bucket-binu'  # Replace with your source bucket name
    destination_bucket = 'new-bucket-binu'  # Replace with your destination bucket name

    # List all objects in the source bucket
    response = s3.list_objects_v2(Bucket=source_bucket)

    if 'Contents' in response:
        for obj in response['Contents']:
            key = obj['Key']
            copy_source = {
                'Bucket': source_bucket,
                'Key': key
            }
            s3.copy_object(CopySource=copy_source, Bucket=destination_bucket, Key=key)

    return {
        'statusCode': 200,
        'body': json.dumps('All data copied successfully!')
    }
