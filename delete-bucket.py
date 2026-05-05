import boto3

BUCKET_NAME = "anant-demo-bucket-ap-south-1"

s3 = boto3.resource('s3')

def delete_bucket(bucket_name):
    bucket = s3.Bucket(bucket_name)

    print("Deleting all object versions (if any)...")
    bucket.object_versions.delete()

    print("Deleting bucket...")
    bucket.delete()

    print("Bucket deleted successfully")

if __name__ == "__main__":
    delete_bucket(BUCKET_NAME)