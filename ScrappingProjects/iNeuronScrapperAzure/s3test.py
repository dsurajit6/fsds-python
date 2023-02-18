import os
import boto3
from botocore.exceptions import ClientError

access_key = 'AKIAWM4UDTOGKDIYAWYZ'
secret = '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'
bucket_name = 'ineuron-course-bucket'

s3_client = boto3.client(
    's3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret
)

file_name = os.path.join(os.getcwd(),'course_files/CompleteDSAinPython.pdf')
try:
    s3_client.upload_file(
        file_name,
        bucket_name,
        'CompleteDSAinPython.pdf'
    )
except ClientError as ce:
    print("Incorrect Credentials")
    print(e)
except Exception as e:
    print(e)

"""
Download
"""
# s3_client.download_file(bucket_name, 'CompleteDSAinPython.pdf', 'CompleteDSAinPython.pdf')