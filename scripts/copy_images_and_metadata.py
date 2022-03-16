from nft_config import PATH
import shutil
import os

def copy_images(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest)

def copy_metadata(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest)

    os.remove(dest + "/_metadata.json") # this file comes from hashlips engine.

def remake_dir(dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)

def copy_images_and_metadata():
    """
    Copy images and metadata that were generated by hashlips engine.
    Run this function in order to overwrite the allocated directories.
    """
    copy_images(PATH["hashlips_images"], PATH["images"])
    copy_metadata(PATH["hashlips_metadata"], PATH["metadata"])

    remake_dir(PATH["contract_URI"])
    remake_dir(PATH["token_URIs"])

def main():
    copy_images_and_metadata()
