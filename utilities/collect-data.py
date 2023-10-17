#!/usr/bin/env python
# tweepy-bots/bots/stream-test.py
from w3lib.url import url_query_cleaner
from url_normalize import url_normalize
from typing import List
import tweepy
import logging
from config import create_api
from random import randint
import time
import os
import pandas as pd
logger = logging.getLogger()


answers = ["Pika Pikachu", "Pi?", "Pi-ka", "Pi-ka-chu?",
           "Pikaaaaaa-chuuuuuu", "Piiiika-chuuuuu", "Pikapikapika... pi-ka",
           "Pipipipipi-chuchuchu", "Chuuu-pika!", "Pikachu-pi", "π-kachu",
           "Pikaaapikaaa", "Piiikaaaachuuuuu", "Pika pika", "pi-i ka Pi-pii-chuuuu pikapi?",
           "pikapi!", "chuuu pi Pi pii Pika-pika", "pi-i pi-ka-chu Pi pii Pikapi", "Meow.. I mean... Pikachu!"]
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
# Subclass Stream to print IDs of Tweets received
api = create_api()
data = []
oldDataLen = 0
banned_users = ["D_Sunny99", "thejapadotxxx", "MassSolemnisZ"]


def canonical_url(u):
    u = url_normalize(u)
    u = url_query_cleaner(u, parameterlist=[
                          'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'], remove=True)

    if u.startswith("http://"):
        u = u[7:]
    if u.startswith("https://"):
        u = u[8:]
    if u.startswith("www."):
        u = u[4:]
    if u.endswith("/"):
        u = u[:-1]
    return u


class IDPrinter(tweepy.Stream):
    def on_status(self, status):
        print(status.text.lower())
        print(status.is_quote_status)
        if status.text.lower().find("rt") != -1:
            print("RETWEET")
        try:
            tData = {"id": status.id, "entities": status.entities, "created_at": status.created_at, "screen_name": status.user.screen_name,
                     "lang": status.lang, "text": status.text, "source": status.source, "source_url": status.source_url,
                     "is_quote_status": status.is_quote_status}
#            print(tData)
            data.append(tData)
            if status.text in ["blowjob", "anal", "sex", "OnlyFans"]:
                print("Sexual content detected")
            if status.user.screen_name in banned_users:
                print("banned user")
            if status.retweeted_status.user.screen_name in banned_users:
                print("banned user")
            print("Is the status possibly_sensitive? : " +
                  str(status.possibly_sensitive))
            print("\n\n/****************************************/\n\n")
        except Exception as e:
            print(e)

        if len(data) % 5 == 0:
            print("Saving CSV")
            df = pd.DataFrame(data)
            df.to_csv("collectedData12:48.csv")


class ConnectionTester(tweepy.Stream):
    def on_connection_error(self):
        df = pd.DataFrame(data)
        df.to_csv("pikachu.csv")
        self.disconnect()


# Initialize instance of the subclass
printer = IDPrinter(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

# Filter realtime Tweets by keyword
printer.filter(track=["pikachu"])
