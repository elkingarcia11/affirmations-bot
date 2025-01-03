from dotenv import load_dotenv
from google.cloud import storage

def get_gcs_bucket(bucket_name):
    # Loading environment variables
    load_dotenv()  
    
    # Create a storage client
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    return bucket

def get_blobs_from(bucket, file_paths):
    blobs = []
    # Download necessary files if not already cached
    for _, input_path in file_paths.items():
        blob = bucket.blob(input_path)
        blobs.append(blob)
    return blobs


def get_blob_from(bucket, file_path):
    blob = bucket.blob(file_path)
    return blob


# Example Usage
"""
BUCKET_NAME = "my-bucket-name"  # Replace with your bucket name
FILE_PATHS = {
    "file1": "path/to/file1.txt",
    "file2": "path/to/file2.txt",
}

# Get the bucket
bucket = get_gcs_bucket(BUCKET_NAME)

# Get the blobs
blobs = get_blobs_from(bucket, FILE_PATHS)

# Print blob names for confirmation
for blob in blobs:
    print(f"Blob: {blob.name}")
"""