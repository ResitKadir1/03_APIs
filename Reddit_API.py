import requests
import Credentials


# ADD VALUES HERE
# get these values by registering an application at https://www.reddit.com/prefs/apps
personal_use_script = Credentials.personal_use_script
secret = Credentials.secret

# create an object to be used for http basic authentication
auth = requests.auth.HTTPBasicAuth(personal_use_script, secret)

# ADD VALUES HERE
# username and password to be placed in the token request
data = {'grant_type': 'password',
        'username': 'rekas12',
        'password': '468855@Bruskk....'}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'data_in_the_wild'}

# send a POST request for an OAuth token
response = requests.post('https://www.reddit.com/api/v1/access_token',
                         auth=auth, data=data, headers=headers)

print(response.json())
# get the access token from the response
oauth_token = response.json()['access_token']

# add the token to the http request header
# the ** operator map the keys of the two dictionaries and add the values
# of the second dict to the first dict
headers = {**headers, **{'Authorization': f'bearer {oauth_token}'}}

# send a request for a resource using the authentication header
response = requests.get('https://oauth.reddit.com/r/wallstreetbets/new', headers=headers)
json_response = response.json()
print(json_response)