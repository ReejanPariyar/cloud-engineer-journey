import boto3

s3 = boto3.resource('s3')

print("Your S3 buckets (via resource):")
for bucket in s3.buckets.all():
    print(f"- {bucket.name}")
