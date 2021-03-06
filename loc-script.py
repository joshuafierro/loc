# New to Python? ->
# To run this file open a terminal here [CTRL + ~ ]
# then type: "python3 [name of your file].py" then press ENTER

import requests
import pprint
import re
import os

urls = ['usteledirec04774x']
iterator = 0
for link in urls:
    try:
        os.makedirs(f'../Desktop/{link}')
    except FileExistsError:
        print("ERROR: Directory already exists. Try renmaing or deleting directory.")
        break
    response = requests.get(f"https://www.loc.gov/item/{link}?fo=json").json()

    for file in response['resources'][0]['files']:

        for obj in file:
            pprint.pprint(obj)
            print('\n')
            if 'info' in obj:
                if obj['mimetype'] == 'image/jp2':
                    image_response = requests.get(obj['url'])
                    iterator = iterator + 1
                    with open(f'../Desktop/{link}/{link}{iterator}.jpeg', 'wb') as fd:
                        fd.write(image_response.content)
                        fd.close()
                else:
                    print("No file found or wrong data type")