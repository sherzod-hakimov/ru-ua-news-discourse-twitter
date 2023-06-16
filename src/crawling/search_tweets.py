import requests
import os
import json
import time
import jsonlines
import tweepy
import pandas as pd
from dateutil import parser

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
## Academic account needed to search for tweets earlier than 30 days
## Academic access tokens ----------------------
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""
BEARER_TOKEN=""

# authorization of consumer key and consumer secret
client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=consumer_key, consumer_secret=consumer_secret,
                access_token=access_token, access_token_secret=access_token_secret)
  
start_time='2022-09-01T00:00:00.000Z'
end_time='2023-01-01T00:00:00.000Z'
max_results=500


def turn_into_dict(object):
    obj = {}
    obj['media_key'] = object.media_key
    obj['height'] = object.height
    obj['width'] = object.width
    obj['duration_ms'] = object.duration_ms
    obj['preview_image_url'] = object.preview_image_url
    obj['type'] = object.type
    obj['url'] = object.url

    return obj


def create_simple_dict(json_response):
    tweet_list = []
    media_dict = {}

    if 'media' in json_response.includes:
        media = json_response.includes['media']
        for md in media:
            md = turn_into_dict(md)
            media_dict[md['media_key']] = md

    try:
        for tweet in json_response.data:
            author_id = tweet.author_id

            created_at = str(tweet.created_at)
            tweet_id = tweet.id
            lang = tweet.lang
            retweet_count = tweet.public_metrics['retweet_count']
            reply_count = tweet.public_metrics['reply_count']
            like_count = tweet.public_metrics['like_count']
            quote_count = tweet.public_metrics['quote_count']
            text = tweet.text
            twt_medias = []

            if 'attachments' in tweet:
                if 'media_keys' in tweet.attachments:
                    media_keys = tweet.attachments['media_keys']

                    for md in media_keys:
                        if md in media_dict:
                            twt_medias.append(media_dict[md])


            tweet_list.append({'tweet_id': tweet_id, 'author_id': author_id, 'created_at': created_at,
                                'lang': lang, 'retweet_count': retweet_count, 'reply_count': reply_count,
                                'like_count': like_count, 'quote_count': quote_count, 'text':text, 'media': twt_medias})
    except:
        print("No data")

    
    return tweet_list


newsmap = pd.read_csv('tweet_crawl_ukraine_war/data/newsmap_all_with_description.csv')
#Get names from april list folder
newsname_set = set([name.split("_1Feb")[0] for name in os.listdir("news_data/1Feb_30Apr_verified")])

for i, row in newsmap.iterrows():
    name = row['Twitter_name']
    idx = row['ID']
    verf = row['Verified']
    fcnt = int(row['Followers'])
    country = row['Country']

    # if verf == True and int(fcnt) >= 100000:
    if name in newsname_set:
        print(name)

        count=0
        flag = True
        next_token = None

        if not os.path.exists('news_data/1Sep_31Dec_verified/%s_1Sep_31Dec.jsonl'%(name)):
            with jsonlines.open('news_data/1Sep_31Dec_verified/%s_1Sep_31Dec.jsonl'%(name), mode='a') as writer:
                while flag:
                    response = client.search_all_tweets(query="from:%s "%(idx), end_time=end_time, expansions="attachments.media_keys", max_results=max_results, 
                    media_fields=["duration_ms","height","width","preview_image_url","url"], 
                    tweet_fields=["author_id","id","text","created_at","lang","attachments","public_metrics"], next_token=next_token, start_time=start_time)

                    json_list = create_simple_dict(response)

                    for obj in json_list:
                        writer.write(obj)
                        count = count + 1

                    if 'next_token' in response.meta:
                        next_token = response.meta['next_token']
                    else:
                        flag = False


                    print(name, count)
                    time.sleep(5)
    

