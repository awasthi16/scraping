import requests
from bs4 import BeautifulSoup

# Step 1: Send request
url = "https://example.com"
response = requests.get(url)

# Step 2: Parse HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract data
title = soup.title.text
print("Website Title:", title)




# ------------------------------
p = soup.find("p")
print(p.text)
# ------------------------------------
links = soup.find_all("a")
for link in links:
    print(link.get("href"))
# -------------------------------------
div = soup.find("div", class_="content")
print(div.text)
# -------------------------------------
main = soup.find(id="main")
print(main.text)
# -----------------------------------------
items = soup.select("ul li")
for item in items:
    print(item.text)
# -----------------------------------------
images = soup.find_all("img")
for img in images:
    print(img.get("src"))
# --------------------------------------------  







soup.title
soup.body
soup.head
soup.p
soup.title.text
soup.title.string
soup.find("p")
soup.find("div", class_="content")
soup.find(id="main")
soup.find_all("a")
soup.find_all("p", class_="text")
soup.find_all("p", limit=3)
soup.select("div")
soup.select(".className")
soup.select("#idName")
soup.select("div p")
tag = soup.find("a")
tag.get("href")
tag["href"]
tag.text
tag.get_text()
tag.get_text(strip=True)



# --------------------------------------



import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

# Website URL
url = "https://example.com"

# Create folder
folder = "images"
os.makedirs(folder, exist_ok=True)

# Get HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all images
images = soup.find_all("img")

for i, img in enumerate(images, start=1):
    img_url = img.get("src")
    
    if not img_url:
        continue

    # Handle relative URLs
    img_url = urljoin(url, img_url)

    # Download image
    img_data = requests.get(img_url).content

    # Save image
    file_path = os.path.join(folder, f"image_{i}.jpg")
    with open(file_path, "wb") as f:
        f.write(img_data)

print("Images saved successfully")
# -----------------------------------------------
import requests
from bs4 import BeautifulSoup
import csv

# Website URL
url = "https://example.com"

# Get webpage
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all <p> tags
paragraphs = soup.find_all("p")

# Create CSV file
with open("paragraphs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Paragraph Text"])   # header

    for p in paragraphs:
        text = p.get_text(strip=True)
        if text:
            writer.writerow([text])

print("Paragraphs saved to paragraphs.csv")

