"""
"""
import os
import requests
import zipfile


def download_data():
    """Download the ePSD2 JSON data to ./json/"""
    # Get the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the URL and download path
    url = "http://oracc.museum.upenn.edu/json/epsd2.zip"
    download_path = os.path.join(script_dir, "epsd2.zip")
    extracted_folder_name = "epsd2"  # The name of the folder that gets extracted

    # Download the zip file
    print("Downloading zip file...")
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get("content-length", 0))

    # Initialize variables for showing progress
    block_size = 1024
    progress_bar_size = 50
    downloaded_size = 0

    with open(download_path, "wb") as f:
        for data in response.iter_content(block_size):
            downloaded_size += len(data)
            f.write(data)

            # Update and print the progress bar
            progress = int(progress_bar_size * downloaded_size / total_size)
            print(
                f"{'#' * progress}{'.' * (progress_bar_size - progress)} {downloaded_size}/{total_size} bytes",
                end="\r",
            )

    print(f"\nDownloaded to {download_path}")

    # Extract the zip file
    print("Extracting zip file...")
    with zipfile.ZipFile(download_path, "r") as zip_ref:
        zip_ref.extractall(script_dir)
    print("Extraction complete.")

    # Delete the zip file
    print("Deleting zip file...")
    os.remove(download_path)
    print("Zip file deleted.")

    # Rename the extracted folder to 'json'
    extracted_folder_path = os.path.join(script_dir, extracted_folder_name)
    downloads_folder_path = os.path.join(script_dir, "json")
    print(f"Renaming folder {extracted_folder_name} to json/")
    os.rename(extracted_folder_path, downloads_folder_path)
