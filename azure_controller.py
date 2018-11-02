req = requests.post('https://brazilsouth.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment',headers={'Content-Type': 'application/json',"Ocp-Apim-Subscription-Key": ""}, json=texto )
print(req.json())
