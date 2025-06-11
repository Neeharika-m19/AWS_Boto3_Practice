import boto3

BUCKET_NAME = "neela-test-1"
s3 = boto3.client("s3")

# List all buckets
buckets_resp = s3.list_buckets()
for bucket in buckets_resp["Buckets"]:
    print(bucket["Name"])  #print just the bucket name

# #Create Bucket
# s3 = boto3.client("s3", region_name="eu-north-1")

# bucket_name = "neela-test-bucket-2"

# bucket_location = s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'eu-north-1'})

# print(bucket_location)

# Upload file to a bucket
# with open("./mountain.jpeg","rb") as f:
# s3.upload_fileobj(f, BUCKET_NAME, "mountain.jpeg")

# Download a File
# s3.download_file(BUCKET_NAME,"mountain.jpeg","downloaded_mountain.jpeg")
    
#List objects in a bucket

response=s3.list_objects_v2(Bucket=BUCKET_NAME)
for obj in response["Contents"]:
    print(obj)