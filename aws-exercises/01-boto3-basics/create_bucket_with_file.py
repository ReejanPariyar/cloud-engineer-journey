import boto3

s3 = boto3.client('s3', region_name='eu-north-1')
bucket_name = "reejan-boto3-automation-test-2026"

s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={'LocationConstraint': 'eu-north-1'}
)

s3.put_object(Bucket=bucket_name, Key="notes.txt",Body="Hello from boto3 automation")
s3.put_object(Bucket=bucket_name, Key="log.txt", Body="Some log content here that is a bit longer")

print(f"Created bucket {bucket_name} with 2 test files")
