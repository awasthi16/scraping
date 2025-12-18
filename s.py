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
