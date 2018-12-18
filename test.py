# Sam Schoberg, 2018

# This program gets the UID for a Fortnite player. It then uses that UID to
# find the player stats. Hope is to eventually integrate into an Amazon Alexa
# skill to humiliate brother. (E.g. "Hey Alexa, how many wins does Luke have
# on Fortnite?")


import json
import requests
url = 'https://fortnite-public-api.theapinetwork.com/prod09/users/id'
payload = {'username': 'Ninja'}
files = {}
headers = {
  'Authorization': '67f308f9b85f67034b3b019fa8f2858c'
}
# Gets JSON object for player
response = requests.request('POST', url, headers = headers, data = payload,
                            files = files, allow_redirects=False, timeout=10)
# Parses JSON object to get UID
response_parsed= json.loads(response.text)

# Gets player stats from UID
url = 'https://fortnite-public-api.theapinetwork.com/prod09/users/public/br_stats'
payload = {'user_id': response_parsed['uid'],
'platform': 'pc',
'window': 'alltime'}
response = requests.request('POST', url, headers = headers, data = payload,
                            files = files, allow_redirects=False, timeout=10)
response_parsed= json.loads(response.text)
print(response_parsed['stats']['placetop1_solo'])
