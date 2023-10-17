#!/usr/bin/env python


import os

# Get a list of the media files extensions inside the specified folder


def getMediaFiles(folder: type[str], extensions: type[list[str]]):
    arr = os.listdir("img/" + folder)
    extensionList = extensions
    mediaList = []
    for fileName in arr:
        for extension in extensionList:
            if fileName.endswith(extension):
                mediaList.append(fileName)
    return mediaList


# Tweet reaction class
class TweetReaction:
    def __init__(self, wordList: type[list[str]], answerReturn: type[str], folderName: type[str]):
        self.wordList = wordList
        self.mediaList = getMediaFiles(
            folderName, ["jpg", "png", "jpeg", "gif"])
        self.answerReturn = answerReturn
        self.folderName = "img/" + folderName + "/"

    def checkIfWordFit(self, text: type[str]) -> bool:
        for word in self.wordList:
            if word in text:
                return True
        return False
