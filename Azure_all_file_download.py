from azure.storage.blob import BlobServiceClient
import os

folder_name = '-qa'
blob_service_client = BlobServiceClient.from_connection_string('DefaultEndpointsProtocol=https;AccountName=your_account;AccountKey=your_key;EndpointSuffix=core.windows.net')
container_client = blob_service_client.get_container_client('')

print(f"Processing folder: {folder_name}")
download_directory = 'temp'
blobs = container_client.list_blobs(name_starts_with=folder_name)

for blob in blobs:
    blob_name = blob.name
    print(f"Processing blob: {blob_name}")

    local_file_path = os.path.join(download_directory, os.path.basename(blob_name))
    local_folder = os.path.dirname(local_file_path)
    os.makedirs(local_folder, exist_ok=True)

    blob_client = container_client.get_blob_client(blob_name)

    with open(local_file_path, "wb") as file:
        file.write(blob_client.download_blob().readall())

    print(f"Downloaded: {blob_name} to {local_file_path}")
