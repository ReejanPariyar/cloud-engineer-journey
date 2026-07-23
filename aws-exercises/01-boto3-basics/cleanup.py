import boto3

s3 = boto3.client('s3', region_name='eu-north-1')
bucket_name = "reejan-boto3-automation-test-2026"

s3.delete_object(Bucket=bucket_name, Key="notes.txt")
s3.delete_object(Bucket=bucket_name, Key="log.txt")
s3.delete_bucket(Bucket=bucket_name)

print(f"Cleaned up and deleted bucket: {bucket_name}")
