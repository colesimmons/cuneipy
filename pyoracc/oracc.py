import os
from typing import List
import requests
import zipfile
from .corpus.enums import CorpusType
from .corpus.exceptions import DownloadError, ExtractionError
from .corpus.models.corpus import Corpus


class Oracc:
    # -----------
    #  Corpus
    # -----------

    _corpus_download_path = "./.corpusdata"

    @property
    def corpus_names(self) -> List[str]:
        """
        Returns a list of available corpora in Oracc.
        """
        return [corpus.value for corpus in CorpusType]

    def download_corpus(self, corpus_name: str) -> None:
        """
        Downloads and extracts a corpus from the Oracc website.

        Args:
            corpus_name (str): The corpus to download.

        Raises:
            DownloadError: If the download fails.
            ExtractionError: If the extraction fails.
        """
        try:
            corpus = CorpusType(corpus_name)
        except ValueError:
            raise ValueError(
                f"Invalid corpus: {corpus_name}. Valid options: {self.corpora}"
            ) from None

        url = corpus.get_download_url()

        os.makedirs(self._corpus_download_path, exist_ok=True)

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

    def load_corpus(self, corpus_name: str) -> List[Corpus]:
        """
        Loads a corpus from the Oracc website.

        Args:
            corpus_name (str): Name of the corpus to load.
        """
        try:
            corpus = CorpusType(corpus_name)
        except ValueError:
            raise ValueError(
                f"Invalid corpus: {corpus_name}. Valid options: {self.corpora}"
            ) from None

        extracted_folder_path = os.path.join(self._corpus_download_path, corpus.value)

        if not os.path.exists(extracted_folder_path):
            raise ValueError(f"Corpus {corpus} has not been downloaded yet.")

        dirs = _find_corpusjson_dirs(extracted_folder_path)
        return Corpus.load(corpus, dirs[0])


def _find_corpusjson_dirs(root_dir: str):
    """Search for the 'corpusjson' dir paths"""
    return [
        root
        for root, _, filenames in os.walk(root_dir)
        if "catalogue.json" in filenames
    ]
