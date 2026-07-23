import boto3

s3 = boto3.client('s3', region_name='eu-north-1')
bucket_name = "reejan-boto3-automation-test-2026"

response = s3.list_objects_v2(Bucket=bucket_name)

files = response.get('Contents', [])
files_sorted = sorted(files, key=lambda x: x['Size'], reverse=True)

print(f"Files in {bucket_name}, sorted by size (largest first):")
for file in files_sorted:
    print(f"- {file['Key']}: {file['Size']} bytes")
