import boto3
import os
BUCKET_NAME = "anant-demo-bucket-ap-south-1"
FILE_NAME = "sample.txt"

s3 = boto3.client('s3')

def create_bucket():
    try:
        s3.create_bucket(
            Bucket=BUCKET_NAME,
            CreateBucketConfiguration={
                'LocationConstraint': 'ap-south-1'
            }
            )
        print("Bucket created form GitHub Actions 🚀")
    except Exception as e:
        print(f"Error creating bucket it may already exist: {e}")


def upload_file():
    with open(FILE_NAME, "w") as f:
        f.write("This file has been created from GitHub Actions 🚀")

    s3.upload_file(FILE_NAME, BUCKET_NAME, FILE_NAME)
    print("File uploaded from GitHub Actions 🚀")

if __name__ == "__main__":
    create_bucket()
    upload_file()