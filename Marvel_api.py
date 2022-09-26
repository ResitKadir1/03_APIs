### Marvel API

import hashlib
import requests
import json
import Credentials
from marvel import Marvel
import os
from datetime import datetime

if not os.path.exists("Marvel_data"):
    os.makedirs("Marvel_data")
Marvel_data = "Marvel_data/"

if not os.path.exists("marvel_pics"):
    os.makedirs("marvel_pics")
marvel_pics = "marvel_pics/"




# the main API endpoint
marvel_endpoint = 'https://gateway.marvel.com/'
# endpoints for specific API calls
marvel_endpoint_comics = marvel_endpoint+'v1/public/comics'
marvel_endpoint_characters = marvel_endpoint+'v1/public/characters'

# ADD VALUES HERE
# the API keys -- you will need them both to compose the API requests
marvel_public_key = Credentials.marvel_public_key
marvel_private_key = Credentials.marvel_private_key


def get_hash(marvel_private_key, marvel_public_key):
    '''
    API requests from "server-side" (meaning: requests coming from a script rather than a website or app)
    require an additional hash to be sent in the GET request. This function calculates this hash
    @param marvel_private_key: your API private key
    @param marvel_public_key: your API public key
    @return a pair (timestamp, hex string representing the hash)
    '''
    # get the current time stamp
    ts = int(datetime.now().timestamp())
    # calculates the hash of the concatenation of ts and keys
    hashcode = hashlib.md5(f'{ts}{marvel_private_key}{marvel_public_key}'.encode()).hexdigest()

    return (ts,hashcode)


###Get Comics
ts, hashcode = get_hash(marvel_private_key, marvel_public_key)

# sends an http GET request with a number of additional parameters in the URL
response = requests.get(
    marvel_endpoint_comics,
    params={'apikey': marvel_public_key,
            'hash': hashcode,
            'ts': ts,
            'offset': 0,
            'format': 'comic',
            'formatType': 'comic',
            'dateRange': '2013-01-01,2013-01-02'
            }
    )


################
# the response is returned as a stream of bytes (we will discuss encodings in one of the next lessons)
json_response = json.loads(response.content.decode('utf8'))
# this is how json responses are saved on file
with open(Marvel_data+'outf.json', 'wt') as outf:
    json.dump(json_response, outf)


############################################
# check the http response code and status
print(json_response['code'], json_response['status'])
# get the response data
data = json_response['data']
# responses are paginated, here a short explanation of what that means:
print(f'This response contains {data["count"]} records (from index {data["offset"]} to index {data["limit"]})')
print(f'But the total number of records available for this request is {data["total"]}')
print(f'To get additional records, issue a new API request with offset starting at {data["limit"]}')



# iterate over the results
character_set = set()
for res in data['results']:
    # extract comic title (similar notation for other fields)
    comic_title = res['title']
    # extract set of characters
    characters = res['characters']['items']
    for c in characters:
        # the character ID is the last segment of the character URI
        character_id = c['resourceURI'].split('/')[-1]
        character_name = c['name']
        character_set.add((character_id, character_name))
print('Set of characters:', character_set)


####GET CHARACTERS

import shutil

for character_id, character_name in character_set:
    print(character_name)
    ts, hashcode = get_hash(marvel_private_key, marvel_public_key)
    # sends an http GET request with a number of additional parameters in the URL
    response = requests.get(
        f'{marvel_endpoint_characters}/{character_id}',
        params={'apikey': marvel_public_key,
                'hash': hashcode,
                'ts': ts
                }
        )
    # get the thumbnail URL
    json_response = json.loads(response.content.decode('utf8'))
    thumb = json_response['data']['results'][0]['thumbnail']
    thumb_url = f'{thumb["path"]}.{thumb["extension"]}'
    # send a regular http request to get the image
    image = requests.get(thumb_url, stream=True)
    # save image on file
    with open(f'marvel_pics/{character_name}.{thumb["extension"]}', 'wb') as out_file:
        shutil.copyfileobj(image.raw, out_file)

"""
#### Marvel API python wrapper
Many API have "wrappers" available in several languages. 
Wrappers are just pieces of code that manage the http requests and handle the responses
 (what we did in the code above), 
so that you can call simple methods to get results directly.

"""


m = Marvel(marvel_public_key, marvel_private_key)
characters = m.characters
character = characters.get(1009189)
print(character)