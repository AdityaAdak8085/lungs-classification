import os
import requests
import gdown
import zipfile
from pathlib import Path
from src.Classifier.utils.common import get_size  # Ensure this function exists
import logging

logger = logging.getLogger(__name__)

class DataIngestion:
    def __init__(self, config):
        self.config = config  # Ensure this is an instance of DataIngestionConfig

    def download_file(self):
        """Downloads a large file from Google Drive using gdown."""
        file_id = "1zoQUChTPfc-2EMBfk0X813bwt0837tQs"
        url = f"https://drive.google.com/uc?export=download&id={file_id}"
        local_file = self.config.local_data_file

        os.makedirs(os.path.dirname(local_file), exist_ok=True)

        try:
            gdown.download(url, local_file, quiet=False)
            print(f"Download successful: {local_file}")

        except Exception as e:
            print(f"Download failed: {e}")
            raise

    def extract_zip_file(self):
        """
        Extracts the ZIP file into the data directory.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        # Ensure the ZIP file exists and is not empty
        if not os.path.exists(self.config.local_data_file) or os.path.getsize(self.config.local_data_file) == 0:
            logger.error("ZIP file is missing or empty. Cannot extract.")
            raise ValueError("ZIP file is missing or empty.")

        try:
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f"Extraction successful! Files extracted to {unzip_path}")

        except zipfile.BadZipFile:
            logger.error("ZIP file is corrupted! Cannot extract.")
            raise ValueError("ZIP file is corrupted.")

