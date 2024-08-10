import requests
from bs4 import BeautifulSoup
import os

# URL of the course page
url = "https://snap.stanford.edu/class/cs224w-2021/"

# Get the HTML content of the page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Create a directory to save the slides
if not os.path.exists('CS224W_Slides'):
    os.makedirs('CS224W_Slides')

# Find all links to slides
for link in soup.find_all('a'):
    href = link.get('href')
    if href and "slides" in href:  # Only consider links containing "slides"
        slide_url = href if href.startswith('http') else url + href
        file_name = os.path.join('CS224W_Slides', href.split('/')[-1])
        
        # Download the slide file
        slide_response = requests.get(slide_url)
        with open(file_name, 'wb') as f:
            f.write(slide_response.content)
        print(f'Downloaded {file_name}')

print("All slides downloaded successfully!")