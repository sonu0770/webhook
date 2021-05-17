import requests
import json

webhook_url = 'https://f34308119943.ngrok.io/webhook'

data ='Hello this is my webhook program'
#data = { 'name': 'DevOps Journey', 
#        'Channel URL': 'test url' }

#r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
if r.status_code == 200:
    print('Success')