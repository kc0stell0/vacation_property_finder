import requests

url = 'https://api.airbnb.com/v2/explore_tabs?_format=for_explore_search_web&currency=USD&items_per_grid=100&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&location=great barrington&section_offset=0&supports_for_you_v3=true&tab_id=home_tab&timezone_offset=300&version=1.3.4'
headers = {'Host': 'api.airbnb.com',
           'Accept-Language': 'en-us',
           'Accept-Encoding': 'gzip, deflate',
           'Accept': 'application / json',
           'Connection': 'keep - alive',
           'X - Airbnb - API - Key': 'd306zoyjsyarp7ifhu67rjxn52tv0t20',
           'X - Airbnb - Carrier - Country': 'us',
           'X - Airbnb - Currency': 'USD',
           'X - Airbnb - Locale': 'en',
           'X - Airbnb - Network - Type': 'wifi'
           }
response = requests.get(url, headers=headers)
print(response.__dict__)
with open('outputfile.json', 'w') as outf:
    outf.write(response.content)
