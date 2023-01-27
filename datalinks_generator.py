from bs4 import BeautifulSoup
import json
from requests_html import HTMLSession


# Create an HTML session
session = HTMLSession()
# Make a request to the web page
response = session.get('https://products.coastalscience.noaa.gov/habs_explorer/index.php?path=TmtxVGduY3JqTXk0dXRrTmZjQ2V0YVlvaTEvczExWEZWK041ZThVRmFlUENRcWRiRFZSWFNOeXRDcTFvME9TNw==&uri=VWtuM1UzbVNVN0RsZzJMeTJvNlNpM29OalF0WTFQQjVZVnpuS3o5bnh1Ym0vYWhtWEh4ck1hREVUamE4SDZ0M2tsd1M1OWg3UDJ0djIrNEkvbXliRUVnSDVvVVVZK1hYZnFTQmdHejlyZDJ4L0g3bkNWM3lubUhaNFdBYVdyRG4=&type=bllEUXA3TmhSK21RVDlqbFYxMmEwdz09')

# Parse the HTML of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the <img> tags on the page
sections = soup.find_all('section', class_='onecol habonecol')

# Extract the links to the images and the alt text (which will be used as the file name)
links = []
for section in sections:
    link = ""
    if section.find('a') is not None and 'href' in section.find('a').attrs:
        link = section.find('a').get('href')

    name = section.text
    links.append({'link': link, 'name': name})

# Print the list of links

# Write the list of links to a JSON file
with open('links.json', 'w') as f:
    json.dump(links, f)

print('links are saved')
