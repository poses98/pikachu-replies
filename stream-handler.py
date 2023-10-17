#!/usr/bin/env python

import tweepy
import logging
import os

from config import create_api
from random import randint
from pprint import pprint
from reactionHandler import handleStatus

logger = logging.getLogger()

# Getting env keys
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
api = create_api()
test = False


# Subclass Stream to print IDs of Tweets received
class IDPrinter(tweepy.Stream):
    def on_status(self, status):
        try:
            if filterStatus(status) == False:
                reaction = handleStatus(status)
                replyToStatus(reaction, status.id)
            else:
                logger.info("WARNING: Not replying\n")
        except Exception as e:
            logger.info(
                "WARNING: not able to send the tweet\nERROR:\n"+e)


# Initialize instance of the subclass
printer = IDPrinter(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)


# Replying the status
def replyToStatus(content, statusId):
    try:
        if type(content) != bool and type(content) != str:
            print(content)
            filename = content.folderName + \
                content.mediaList[randint(0, len(content.mediaList)-1)]
            media_id = api.media_upload(filename).media_id
            api.update_status(content.answerReturn, media_ids=[media_id], in_reply_to_status_id=statusId,
                              auto_populate_reply_metadata=True)
        elif test:
            print(content)
            api.update_status(content, in_reply_to_status_id=statusId,
                              auto_populate_reply_metadata=True)
    except Exception as e:
        print(e)


def filterStatus(status) -> bool:
    check = False
    if status.user.screen_name == "pikachuReplies":
        check = True
    if status.text.lower().find("pikachu") == -1:
        check = True
    if status.text.lower().find("rt") != -1:
        check = True
    return check


try:
    # Filter realtime Tweets by keyword
    printer.filter(track=["pikachu"])
except Exception as e:
    print(e)
