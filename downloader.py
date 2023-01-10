import requests
from bs4 import BeautifulSoup
import json
from requests_html import HTMLSession

def get_url_paths(url):
    # Create an HTML session
    session = HTMLSession()
    #    Make a request to the web page
    response = session.get(url)
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
    return



Data_path = {
       'GreenBay':'https://products.coastalscience.noaa.gov/habs_explorer/index.php?path=OWxwWDYyYVdTbEFwV2I2RnJUZytYb2h4N2VyVDczMGRDYU9xRWd4TFMvN2I1bkN1Z2NzNU83b2hvTHgrL1BmcA==&uri=VWtuM1UzbVNVN0RsZzJMeTJvNlNpM29OalF0WTFQQjVZVnpuS3o5bnh1Ym0vYWhtWEh4ck1hREVUamE4SDZ0M2tsd1M1OWg3UDJ0djIrNEkvbXliRU5jWkc4MUYwcU1wRFJEVEsvaWNIL0ZQN041NkU0YTB6blpwb0xyb0o0cTg=&type=bllEUXA3TmhSK21RVDlqbFYxMmEwdz09',
       'SiginawBay':'https://products.coastalscience.noaa.gov/habs_explorer/index.php?path=TmtxVGduY3JqTXk0dXRrTmZjQ2V0YVlvaTEvczExWEZWK041ZThVRmFlUENRcWRiRFZSWFNOeXRDcTFvME9TNw==&uri=VWtuM1UzbVNVN0RsZzJMeTJvNlNpM29OalF0WTFQQjVZVnpuS3o5bnh1Ym0vYWhtWEh4ck1hREVUamE4SDZ0M2tsd1M1OWg3UDJ0djIrNEkvbXliRUVnSDVvVVVZK1hYZnFTQmdHejlyZDJ4L0g3bkNWM3lubUhaNFdBYVdyRG4=&type=bllEUXA3TmhSK21RVDlqbFYxMmEwdz09',
       'WesternLake':'https://products.coastalscience.noaa.gov/habs_explorer/index.php?path=RUIvWnB3dWJmS3RvNXlWcjF4a1hLM1B0eERkak1wT2hueTFPRjFMSzVyQmJYMjVpQ2NmUzk5eVllQlVQd1ZiTw==&uri=VWtuM1UzbVNVN0RsZzJMeTJvNlNpM29OalF0WTFQQjVZVnpuS3o5bnh1Ym0vYWhtWEh4ck1hREVUamE4SDZ0M2tsd1M1OWg3UDJ0djIrNEkvbXliRUpBLzVSc3NaMVRvY3I5TG9ISjNTM2E4dDVNRzVZNmt2TjBVMHF5dUtha2s=&type=bllEUXA3TmhSK21RVDlqbFYxMmEwdz09',
       'Albemarle':'https://products.coastalscience.noaa.gov/habs_explorer/index.php?path=ampYVkFlcUd6MG9tYkZqNTNoUmZDajBLU0ttckdvd0JXWG9TVHFPQWxPK3RBM1J1a1crZGN0Sm5RZm0vZ3RwZw==&uri=VWtuM1UzbVNVN0RsZzJMeTJvNlNpM29OalF0WTFQQjVZVnpuS3o5bnh1Ym0vYWhtWEh4ck1hREVUamE4SDZ0M2tsd1M1OWg3UDJ0djIrNEkvbXliRU9TbWNHY2k4TW02RjN4eGFQNkUzOG5TWld1N2pWdlQzaWhDeCtKUktncXk=&type=bllEUXA3TmhSK21RVDlqbFYxMmEwdz09',
       'Pontchartrain':'https://products.coastalscience.noaa.gov/habs_explorer/index.php?path=NUxCRFRyTDVBY2VQWkEvS3hadTlBeHVhdUw4Mm52dUR0LzJYNUhMckdSR0h1dFRWMmRKb2p3a2ZFT2ZoV1pmMw==&uri=VWtuM1UzbVNVN0RsZzJMeTJvNlNpM29OalF0WTFQQjVZVnpuS3o5bnh1Ym0vYWhtWEh4ck1hREVUamE4SDZ0M2tsd1M1OWg3UDJ0djIrNEkvbXliRUg2S3lveTJyVzZoSHI5bEcxVlNGVkNzTEpPSFBPb0lSTXRoSG9TemVYMEhBdTZzQXdlNUhPaSs0M0NPa0t5VmF3PT0=&type=bllEUXA3TmhSK21RVDlqbFYxMmEwdz09',
       'Okeechobee':'https://products.coastalscience.noaa.gov/habs_explorer/index.php?path=ajZiOVoxaHZNdE5nNytEb3RZdU5iYjNnK3AvTWRrYmNWbXU0K0YvMlA1UlBtTWZlRFV3R1RicVRYb2pxeVJBUA==&uri=VWtuM1UzbVNVN0RsZzJMeTJvNlNpM29OalF0WTFQQjVZVnpuS3o5bnh1Ym0vYWhtWEh4ck1hREVUamE4SDZ0M2tsd1M1OWg3UDJ0djIrNEkvbXliRUJ3WjkrKzdIcUYrN1JsZ1I5NFlsaHBZbUJWV0pHZ3NFZUVnQW56aTFIbEw=&type=bllEUXA3TmhSK21RVDlqbFYxMmEwdz09',
       'Florida':'https://products.coastalscience.noaa.gov/habs_explorer/index.php?path=ajZiOVoxaHZNdE5nNytEb3RZdU5iWGNKSlhTQmVYUGUrb0piaTB5QnhOMXhuenIxN1FQU2orR0sxbkNwejhMaQ==&uri=VWtuM1UzbVNVN0RsZzJMeTJvNlNpM29OalF0WTFQQjVZVnpuS3o5bnh1Ym0vYWhtWEh4ck1hREVUamE4SDZ0M2tsd1M1OWg3UDJ0djIrNEkvbXliRUVkQkpRdFJDdjFkbTRoaUQ2L3J0UmpKYzNzMVVkc2ZCKy9nREM1R2FTcFU=&type=bllEUXA3TmhSK21RVDlqbFYxMmEwdz09'
       }

ext = '.tif'

get_url_paths(Data_path['GreenBay'])


# =============================================================================
# # Create an HTML session
# session = HTMLSession()
# # Make a request to the web page
# response = session.get('https://products.coastalscience.noaa.gov/habs_explorer/index.php?path=TmtxVGduY3JqTXk0dXRrTmZjQ2V0YVlvaTEvczExWEZWK041ZThVRmFlUENRcWRiRFZSWFNOeXRDcTFvME9TNw==&uri=VWtuM1UzbVNVN0RsZzJMeTJvNlNpM29OalF0WTFQQjVZVnpuS3o5bnh1Ym0vYWhtWEh4ck1hREVUamE4SDZ0M2tsd1M1OWg3UDJ0djIrNEkvbXliRUVnSDVvVVVZK1hYZnFTQmdHejlyZDJ4L0g3bkNWM3lubUhaNFdBYVdyRG4=&type=bllEUXA3TmhSK21RVDlqbFYxMmEwdz09')
# 
# # Parse the HTML of the page
# soup = BeautifulSoup(response.text, 'html.parser')
# 
# # Find all the <img> tags on the page
# sections = soup.find_all('section', class_='onecol habonecol')
# 
# # Extract the links to the images and the alt text (which will be used as the file name)
# links = []
# for section in sections:
#     link = ""
#     if section.find('a') is not None and 'href' in section.find('a').attrs:
#         link = section.find('a').get('href')
# 
#     name = section.text
#     links.append({'link': link, 'name': name})
# 
# # Print the list of links
# 
# # Write the list of links to a JSON file
# with open('links.json', 'w') as f:
#     json.dump(links, f)
# 
# print('links are saved')
# =============================================================================

# =============================================================================
# def save_file():
#     result = get_url_paths(url, ext)
#     for file in result:
#         f_name = file[-19:-13]
#         # f_name = file[-12:-4]
#         r = requests.get(file)
#         # r = requests.get(file, auth=HTTPBasicAuth('username', 'password'))
#         with open(f'D:\USA_Lakes\GreenBay', 'wb') as f:
#             f.write(r.content)
# =============================================================================
            