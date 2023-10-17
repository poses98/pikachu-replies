#!/usr/bin/env python

from collections import Counter
import csv
from pprint import pprint
# counts word frequency


def count_words(text):
    skips = [".", ", ", ":", ";", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

    # >>>count_words(text) You can check the function

# counts word frequency using
# Counter from collections


def count_words_fast(text):
    text = text.lower()
    skips = [".", ", ", ":", ";", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = Counter(text.split(" "))
    return word_counts


my_list = []


def fillCsv():
    with open('pikachu.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            my_list.append(row)


def wordInText(wordList, text):
    for word in wordList:
        if word in text:
            return True
    return False


print("[")
i = 1
while i < 5:
    print("\"fly" + str(i)+".gif\",")
    i += 1
print("]")
