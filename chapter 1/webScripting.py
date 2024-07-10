#  Web Scraping
# Libraries: BeautifulSoup, scrapy (optional)

# Concepts: Extracting information from web pages, navigating through HTML structures.


from bs4 import BeautifulSoup
import requests

# Make an HTTP GET request to fetch the webpage
response = requests.get('https://example.com')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract and print the title of the webpage
    print(soup.title.text)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
