import requests
from bs4 import BeautifulSoup
import os
import urllib

def download_content(profile_url, download_folder):
    response = requests.get(profile_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all('img', {'decoding': 'auto'}) + soup.find_all('video', {'preload': 'auto'})

    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    for i, element in enumerate(elements):
        src = element.get('src')
        if src:
            if 'image' in src:
                extension = 'jpg'
            elif 'video' in src:
                extension = 'mp4'
            else:
                continue

            filename = f"media_{i}.{extension}"
            urllib.request.urlretrieve(src, os.path.join(download_folder, filename))

if __name__ == "__main__":
    # Set the profile URL of the account from which you want to download content
    profile_url = "https://www.instagram.com/fresh_spar/"

    # Set the folder where you want to download the content
    download_folder = "instagram_content"

    # Download content
    download_content(profile_url, download_folder)

    print("Download completed.")
