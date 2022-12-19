import os

from minio import Minio
from minio.error import InvalidResponseError

accessID = os.environ.get('MINIO_ROOT_USER')
accessSecret = os.environ.get('MINIO_ROOT_PASSWORD')
minioUrl = os.environ.get('MLFLOW_S3_ENDPOINT_URL')
bucketName = os.environ.get('MLFLOW_BUCKET_NAME')

if accessID == None:
    print('[!] AWS_ACCESS_KEY_ID environment variable is empty! run \'source .env\' to load it from the .env file')
    exit(1)

if accessSecret == None:
    print('[!] AWS_SECRET_ACCESS_KEY environment variable is empty! run \'source .env\' to load it from the .env file')
    exit(1)

if minioUrl == None:
    print('[!] MLFLOW_S3_ENDPOINT_URL environment variable is empty! run \'source .env\' to load it from the .env file')
    exit(1)


if bucketName == None:
    print('[!] AWS_BUCKET_NAME environment variable is empty! run \'source .env\' to load it from the .env file')
    exit(1)

minioUrlHostWithPort = minioUrl.split('//')[1]
print('[*] minio url: ', minioUrlHostWithPort)

s3Client = Minio(
    minioUrlHostWithPort,
    access_key=accessID,
    secret_key=accessSecret,
    secure=False
)

# # Check if the bucket already exists
# if s3Client.bucket_exists(bucketName):
#     # Delete all objects in the bucket
#     objects = s3Client.list_objects(bucketName, recursive=True)
#     for obj in objects:
#         s3Client.remove_object(bucketName, obj.object_name)
#     # Delete the bucket
#     s3Client.remove_bucket(bucketName)

# # Create a new bucket with the same name
# s3Client.make_bucket(bucketName)

# try:
#     # Create the bucket
#     s3Client.make_bucket(bucketName)
# except minio.error.S3Error as e:
#     if e.code == "BucketAlreadyOwnedByYou":
#         print("Bucket '{}' already exists and is owned by you".format(bucketName))
#     else:
#         # Handle other S3 errors
#         raise e
