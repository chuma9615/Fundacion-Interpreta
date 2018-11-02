import requests
import json
import base64
import random
import twitter
import datetime
from brandwatch import *
from twitter_controller import *
from azure_controller import *

#print(texto)
req = requests.post('https://brazilsouth.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment',headers={'Content-Type': 'application/json',"Ocp-Apim-Subscription-Key": "734c1105a3cc4a12a8110de0c7f2b33f"}, json=texto )
print(req.json())
