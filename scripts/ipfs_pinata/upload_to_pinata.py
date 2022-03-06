from scripts.helpful_scripts import PINATA_API_KEY, PINATA_API_SECRET
from pathlib import Path
import requests

def upload_to_pinata(filepath=None):

    """
    Use pinata if your IPFS server will not be running all the time.
    So the viewers will be able to see the image and the metadata
    of an NFT whenever they would like to.
    """

    PINATA_BASE_URL = "https://api.pinata.cloud/"
    endpoint = "pinning/pinFileToIPFS"
    filename = filepath.split("/")[-1:][0] # slicing path to name of file.
    headers = {
        "pinata_api_key": PINATA_API_KEY,
        "pinata_secret_api_key": PINATA_API_SECRET
    }

    with Path(filepath).open("rb") as fp:
        file_binary = fp.read()
        response = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": (filename, file_binary)},
            headers=headers,
        )
        ipfs_hash = response.json()["IpfsHash"]
        # "./img/0-COOL.png" -> "0-COOL.png"
        filename = filepath.split("/")[-1:][0]
        file_uri = f"ipfs://{ipfs_hash}?filename={filename}"

        print(f"Successfully uploaded {filename} to pinata.")
        print(file_uri)

        return file_uri

def main():
    upload_to_pinata()