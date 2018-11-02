api = twitter.Api(consumer_key='paUpFJeIDGoXUpKCliEduiiYR',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='',tweet_mode='extended')
tweets = api.GetStatuses(twit_id)
texto = {'documents':[]}
#print(tweets)
for tweet in tweets:
    if tweet.retweeted_status is None:
        print(tweet.full_text)
        print(tweet.id)
        print()
        item = {'id':tweet.id ,'language': 'es','text': tweet.full_text }
    else:
        print(tweet.retweeted_status.full_text)
        print(tweet.retweeted_status.id)
        print()
        item = {'id':tweet.retweeted_status.id ,'language': 'es','text': tweet.retweeted_status.full_text }

    texto['documents'].append(item)
