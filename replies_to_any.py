#!/usr/bin/env python

import tweepy
import logging
from config import create_api
from random import randint
import time
import os

from models.TweetReaction import TweetReaction

logger = logging.getLogger()

answers = ["Pika Pikachu", "Pi?", "Pi-ka", "Pi-ka-chu?",
           "Pikaaaaaa-chuuuuuu", "Piiiika-chuuuuu", "Pikapikapika... pi-ka",
           "Pika pika... pika pika piiii", "Chuuu-pika!", "Pikachu-pi", "π-kachu",
           "Pikaaapikaaa", "Piiikaaaachuuuuu", "Pika pika", "pi-ka-chuuuu pikapi?",
           "Pikapi!", "Pi-ka?", "Pikachu?"]

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
# Subclass Stream to print IDs of Tweets received
api = create_api()

banned_users = ["D_Sunny99", "thejapadotxxx", "MassSolemnisZ", "van51681889"]

pikachu_surprise = [
    "surprisepikachu1.jpg",
    "surprisepikachu2.png",
    "surprisepikachu3.jpg",
    "surprisepikachu4.jpeg",
    "surprisepikachu5.png",
    "surprisepikachu6.jpg",
    "surprisepikachu7.jpg",
    "surprisepikachu8.jpg",
    "surprisepikachu9.jpeg",
    "surprisepikachu10.gif",
    "surprisepikachu11.jpg",
    "surprisepikachu12.gif",
]
cutepikachu = [
    "cute1.gif",
    "cute2.gif",
    "cute3.gif",
    "cute4.gif",
    "cute5.gif",
    "cute6.gif",
    "cute7.gif",
]
irontail = [
    "irontail1.gif",
    "irontail2.gif",
    "irontail3.gif",
    "irontail4.gif",
]
thunderbolt = [
    "thunderbolt1.gif",
    "thunderbolt2.gif",
    "thunderbolt3.gif",
]
happypikachu = [
    "happypikachu1.gif",
    "happypikachu2.gif",
    "happypikachu3.gif",
    "happypikachu4.gif",
    "happypikachu6.gif",
]
surfpikachu = [
    "surf1.gif",
    "surf2.gif",
    "surf3.gif",
    "surf4.gif",
    "surf5.gif",
    "surf6.gif",
]
flypikachu = [
    "fly1.gif",
    "fly2.gif",
    "fly3.gif",
    "fly4.gif",
]


class IDPrinter(tweepy.Stream):
    def on_status(self, status):
        if status.user.name != "Pikachu Replies":
            print("\n"+str(status.id))
            print(status.created_at)
            print("user name: " + status.user.name)
            print("screen name: " + status.user.screen_name)
            print("text: " + status.text)
            indexOfAnswer = randint(0, len(answers)-1)
            try:
                check = False
                answer = answers[indexOfAnswer]
                # Checking if the tweet contains pikachu
                if status.text.lower().find("pikachu") == -1:
                    print("Pikachu not found.")
                    check = True
                    # Checking if the tweet is a retweet
                if status.text.lower().find("rt") != -1:
                    print("This is a retweet.")
                    check = True
                # Looking for banned words
                if status.text.lower() in ["blowjob", "anal", "sex", "onlyfans", "cum"]:
                    print("Sexual content detected")
                    check = True
                # Checking if the user has been already banned
                if status.user.screen_name in banned_users:
                    print("Banned user")
                    check = True
                # Checking for surprise pikachu
                # if (status.text.lower().find("surprise") != -1 or status.text.lower().find("surprised") != -1 or status.text.lower().find("shocked") != -1):
                #    answer = "surprise"
                # Checking for cute pikachu or love
                if (status.text.lower().find("adorable") != -1 or status.text.lower().find("cute") != -1 or status.text.lower().find("lindo") != -1 or status.text.lower().find("amo") != -1):
                    #answer = "cute"
                    print("CUTE word detected")
                 # Checking for Pikachu I choose you
                if (status.text.lower().find("thunder") != -1 or status.text.lower().find("thunderbolt") != -1):
                    answer = "thunderbolt"

                 # Checking for Pikachu I choose you
                if (status.text.lower().find("choose you") != -1 or status.text.lower().find("elijo a ti") != -1):
                    answer = "choose you"

                # Checking for iron tail
                if status.text.lower().find("iron tail") != -1 or status.text.lower().find("cola ferrea") != -1:
                    answer = "iron-tail"

                if status.text.lower().find("use surf") != -1 or status.text.lower().find("surf") != -1:
                    answer = "surf"

                if status.text.lower().find("use fly") != -1 or status.text.lower().find("fly") != -1:
                    answer = "fly"

                if check == False:
                    reply_to_status(answer, status)
                else:
                    print("WARNING: Not replying\n")
            except:
                logger.info("\n\nWARNING: not able to send the tweet\n\n")


                # Initialize instance of the subclass
printer = IDPrinter(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)


def reply_to_status(text, status):
    try:
        if text == "surprise":
            print("surprise pikachu")
            filename = "img/surprisepikachu/" + \
                pikachu_surprise[randint(0, len(pikachu_surprise)-1)]
            media_id = api.media_upload(filename).media_id
            api.update_status("Pi-ka-chu?", media_ids=[media_id], in_reply_to_status_id=status.id,
                              auto_populate_reply_metadata=True)
        elif text == "iron-tail":
            print("Sending iron tail!")
            filename = "img/irontail/" + \
                irontail[randint(0, len(irontail)-1)]
            media_id = api.media_upload(filename).media_id
            api.update_status("Chuuuu-pika!", media_ids=[media_id], in_reply_to_status_id=status.id,
                              auto_populate_reply_metadata=True)
        elif text == "thunderbolt":
            print("Thunderbolt attack!")
            filename = "img/thunderbolt/" + \
                thunderbolt[randint(0, len(thunderbolt)-1)]
            media_id = api.media_upload(filename).media_id
            api.update_status("Piiiiikaaaa-chuuuuuu", media_ids=[media_id], in_reply_to_status_id=status.id,
                              auto_populate_reply_metadata=True)
        elif text == "cute":
            print("I am cute!")
            filename = "img/cutepikachu/" + \
                cutepikachu[randint(0, len(cutepikachu)-1)]
            media_id = api.media_upload(filename).media_id
            api.update_status("Pika💕", media_ids=[media_id], in_reply_to_status_id=status.id,
                              auto_populate_reply_metadata=True)
        elif text == "choose you":
            print("I choose you!")
            filename = "img/happypikachu/" + \
                happypikachu[randint(0, len(happypikachu)-1)]
            media_id = api.media_upload(filename).media_id
            api.update_status("Pika pi!!!", media_ids=[media_id], in_reply_to_status_id=status.id,
                              auto_populate_reply_metadata=True)
        elif text == "fly":
            print("I can fly!")
            filename = "img/fly/" + \
                flypikachu[randint(0, len(flypikachu)-1)]
            media_id = api.media_upload(filename).media_id
            api.update_status("Pikachuuuu pikaaa", media_ids=[media_id], in_reply_to_status_id=status.id,
                              auto_populate_reply_metadata=True)
        elif text == "surf":
            print("I can surf!")
            filename = "img/surfpikachu/" + \
                surfpikachu[randint(0, len(surfpikachu)-1)]
            media_id = api.media_upload(filename).media_id
            api.update_status("Pika!! Pikapiiii", media_ids=[media_id], in_reply_to_status_id=status.id,
                              auto_populate_reply_metadata=True)
        else:
            api.update_status(
                # GET RESPONSE FROM JSON FILE RANDOMLY
                status=text,
                in_reply_to_status_id=status.id,
                auto_populate_reply_metadata=True
            )
    except Exception as e:
        print(e)


def updateStatusWithPicture():
    try:
        filename = "img/gifs/pikachu_iron_tail.gif"
        media_id = api.media_upload(filename).media_id
        api.update_status("Piiiikaaa", media_ids=[media_id])
    except Exception as e:
        print(e)


# Filter realtime Tweets by keyword
printer.filter(track=["pikachu"])
