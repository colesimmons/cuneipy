import os
from typing import List
import requests
import zipfile
from .constants import Corpus
from .exceptions import DownloadError, ExtractionError


class Oracc:
    # -----------
    #  Corpus
    # -----------

    _corpus_download_path = "./corpusdata"

    @property
    def corpora(self) -> List[str]:
        """
        Returns a list of available corpora in Oracc.
        """
        return [corpus.value for corpus in Corpus]

    def download_corpus(self, corpus: Corpus) -> None:
        """
        Downloads and extracts a corpus from the Oracc website.

        Args:
            corpus (Corpus): The corpus to download.

        Raises:
            DownloadError: If the download fails.
            ExtractionError: If the extraction fails.
        """
        url = corpus.get_download_url()

        zip_file_name = os.path.basename(url)
        zip_file_path = os.path.join(self._corpus_download_path, zip_file_name)
        extracted_folder_path = os.path.join(self._corpus_download_path, corpus.value)

        if os.path.exists(extracted_folder_path):
            return

        # Download the .zip
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for bad responses

            with open(zip_file_path, "wb") as f:
                f.write(response.content)
        except requests.RequestException as e:
            raise DownloadError(
                f"Failed to download .zip for {corpus}. Reason: {str(e)}"
            )

        # Extract the .zip
        try:
            with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
                zip_ref.extractall(extracted_folder_path)
        except zipfile.BadZipFile as e:
            raise ExtractionError(
                f"Failed to extract .zip for {corpus}. Reason: {str(e)}"
            )

        # Remove the .zip
        os.remove(zip_file_path)

    def load_corpus(self, corpus: Corpus):
        """
        Loads a corpus from the Oracc website.

        Args:
            corpus (Corpus): The corpus to load.
        """
        extracted_folder_path = os.path.join(self._corpus_download_path, corpus.value)

        if not os.path.exists(extracted_folder_path):
            raise ValueError(f"Corpus {corpus} has not been downloaded yet.")

        return
