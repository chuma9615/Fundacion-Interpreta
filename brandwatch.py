re = requests.post(
            'https://newapi.brandwatch.com/' + "oauth/token?",
            params={
                "username": 'nacho@interpreta.org',
                "password": '',
                "grant_type": 'api-password',
                "client_id": 'brandwatch-api-client'
            })
token = re.json()['access_token']
print(token)
apiurl = 'https://api.brandwatch.com/'
re = requests.get('https://api.brandwatch.com/projects/summary',params={'access_token': token}).json()
print(re)
for resul in re["results"]:
    if resul["name"] == 'MEGA':
        id_proyecto= resul['id']

re = requests.get(apiurl +'projects/'+str(id_proyecto)+ '/queries/summary',params={'access_token': token} ).json()
for resul in re["results"]:
    #print(resul)
    if resul["name"] == 'Mega':
        id_query= resul['id']
        break

today = datetime.date.today()
yesterday = today - datetime.timedelta(30)
print(yesterday)

re = requests.get(apiurl +'projects/'+str(id_proyecto)+ '/data/mentions?',params={'pageType':'twitter','endDate':today,'startDate':yesterday,'queryId':str(id_query),'access_token': token} ).json()
twit_id = []
print(re)
for results in re['results']:
    print(results)
    twit_id.append(results['url'].split("/")[-1])
