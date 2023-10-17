#!/usr/bin/env python

from random import randint
from models.TweetReaction import TweetReaction
from models.TweetReactionManager import TweetReactionManager

reactionManager = TweetReactionManager()

# Surprise
reactionManager.addReaction(TweetReaction(
    folderName="surprisepikachu",
    wordList=["shocked", "surprise",
              "surprised", "sorpresa"],
    answerReturn="Pi-ka-chu?"))
# Cute
reactionManager.addReaction(TweetReaction(
    folderName="cutepikachu",
    wordList=["adorable", "cute",
              "lindo", "love"],
    answerReturn="Pika piiii"))
# Choose you
reactionManager.addReaction(TweetReaction(
    folderName="happypikachu",
    wordList=["choose you", "elijo a ti"],
    answerReturn="Pika pika!"))
# Volt tackle
reactionManager.addReaction(TweetReaction(
    folderName="volt-tackle",
    wordList=["volt tackle", "placaje electrico", "placaje eléctrico"],
    answerReturn="Pikapikapika... pi-ka!"))
# Thunder
reactionManager.addReaction(TweetReaction(
    folderName="thunderbolt",
    wordList=["thunder", "thunderbolt",
              "rayo", "trueno", "/thunder", "/thunderbolt", "/trueno", "/rayo", "/impactrueno"],
    answerReturn="Piiiiiikaaaa-chuuuuuu"))
# Iron tail
reactionManager.addReaction(TweetReaction(
    folderName="irontail",
    wordList=["iron tail", "cola ferrea", "cola férrea"],
    answerReturn="Chuuuu-pika!"))
# Surf
reactionManager.addReaction(TweetReaction(
    folderName="surfpikachu",
    wordList=["surf"],
    answerReturn="Pika!! Pikapiiii"))
# Fly
reactionManager.addReaction(TweetReaction(
    folderName="fly",
    wordList=["fly", "vuelo", "volador"],
    answerReturn="Pikachuuuu pikaaa"))
# Agility
reactionManager.addReaction(TweetReaction(
    folderName="agility",
    wordList=["agility", "agilidad"],
    answerReturn="Pika pika!"))
# Team Rocket
reactionManager.addReaction(TweetReaction(
    folderName="teamrocket",
    wordList=["team rocket"],
    answerReturn="Pi-ka-chu"))
# Talk
reactionManager.addReaction(TweetReaction(
    folderName="talk",
    wordList=["pikachu talk", "pikachu habla", "habla pikachu"],
    answerReturn="Pika pika pika pika... pikaaaa Pikachu"))
# Dance
reactionManager.addReaction(TweetReaction(
    folderName="dance",
    wordList=["dance", "baila", "baile"],
    answerReturn="Pika pikachu!! Pika pika pika"))
# Detective
reactionManager.addReaction(TweetReaction(
    folderName="detectivepikachu",
    wordList=["detective"],
    answerReturn="Pikachu! Pika pika pi!"))
# Creepy
reactionManager.addReaction(TweetReaction(
    folderName="creepy",
    wordList=["creepy", "revenge", "vengate",
              "véngate", "venganza", "asesina", "kill"],
    answerReturn="Pi... ka..."))
# Bunch of pika pika
pikaLanguage = ["Pika Pikachu", "Pi?", "Pi-ka", "Pi-ka-chu?",
                "Pikaaaaaa-chuuuuuu", "Piiiika-chuuuuu", "Pikapikapika... pi-ka",
                "Pika pika... pika pika piiii", "Chuuu-pika!", "Pikachu-pi", "π-kachu",
                "Pikaaapikaaa", "Piiikaaaachuuuuu", "Pika pika", "pi-ka-chuuuu pikapi?",
                "Pikapi!", "Pi-ka?", "Pikachu?"]


def handleStatus(status):
    if reactionManager.checkTextForReaction(status.text.lower()):
        return reactionManager.reaction
    else:
        return pikaLanguage[randint(0, len(pikaLanguage)-1)]
