# Data Parsing
# Libraries: BeautifulSoup (from bs4), json

# Concepts: Parsing HTML responses, extracting specific data, handling JSON re

from bs4 import BeautifulSoup # type: ignore
import json

# Parsing HTML
html = '<html><body><h1>Hello, world!</h1></body></html>'
soup = BeautifulSoup(html, 'html.parser')

# Extract and print the text inside the <h1> tag
print(soup.h1.text)

# Handling JSON
json_data = '{"name": "John", "age": 30}'
data = json.loads(json_data)

# Extract and print the value associated with the 'name' key
print(data['name'])


# o/p :

# Hello, world!
# John

