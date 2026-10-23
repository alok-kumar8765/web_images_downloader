import os
from urllib.parse import urlparse, urljoin
import requests
from bs4 import BeautifulSoup

url = input("Enter Website URL : ")
os.makedirs("images", exist_ok=True)

# Standard browser header to prevent bot blocking (403 errors)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
except Exception as e:
    print(f"Failed to fetch the main webpage: {e}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

for i, img in enumerate(soup.find_all("img", src=True), 1):
    image_url = urljoin(url, img["src"])

    try:
        img_response = requests.get(image_url, headers=headers, timeout=10)
        img_response.raise_for_status()

        # Extract file extension from URL path, default to .jpg if missing/invalid
        parsed_path = urlparse(image_url).path
        ext = os.path.splitext(parsed_path)[1]
        if not ext or len(ext) > 5:
            ext = ".jpg"

        filename = f"images/image_{i}{ext}"
        
        # Fixed: changed .contents to .content
        with open(filename, "wb") as f:
            f.write(img_response.content)
            
        print("Saved :", filename)
    except Exception as e:
        print("Skipped :", image_url, "->", e)