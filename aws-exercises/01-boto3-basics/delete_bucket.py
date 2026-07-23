import boto3

s3 = boto3.client('s3', region_name='eu-north-1')

bucket_name = "reejan-boto3-practice-bucket-2026"

s3.delete_bucket(Bucket=bucket_name)

print(f"Deleted bucket: {bucket_name}")
