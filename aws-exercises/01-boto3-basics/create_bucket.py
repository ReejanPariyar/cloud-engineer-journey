import boto3
 
s3 = boto3.client('s3', region_name='eu-north-1')

bucket_name = "reejan-boto3-practice-bucket-2026"

s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={'LocationConstraint': 'eu-north-1'}
)

print(f"Created bucket: {bucket_name}")

