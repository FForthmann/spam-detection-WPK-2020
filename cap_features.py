import csv

import numpy as np
from _operator import contains
from ntpath import split
from pip._vendor.packaging.tags import Tag


def amount_cap_words(inputtext):
    splittext = inputtext.split(" ")
    total = 0
    first = ""
    for word in splittext:
        if (len(word) > 0):
            first = word[0]
            if first.isupper():
                total += 1
    return_dict = {'values': [total], 'heads': ['@Attribute amount_cap_words REAL']}
    return return_dict


def cap_word_ratio(inputtext):
    splittext = inputtext.split(" ")
    total = 0
    first = ""
    for word in splittext:
        if (len(word) > 0):
            first = word[0]
            if first.isupper():
                total += 1
    total_cap_words = float(total)
    amount_words = float(len(splittext))

    return_dict = {'values': [total_cap_words / amount_words], 'heads': ['@Attribute cap_word_ratio REAL']}
    return return_dict


def spammy_words(inputtext):
    with open('spammy_words_list_general.csv', newline='') as f:
        reader = csv.reader(f)
        spam_words = list(reader)

    spam_words = np.array(spam_words)
    spam_words = spam_words.flatten()

    splittext = inputtext.split(" ")
    total = 0
    for word in spam_words:
        total += splittext.count(word)

    total_spammy_words = float(total)

    return_dict = {'values': [total], 'heads': ['@Attribute spammy_words REAL']}
    return return_dict


def html_tag_count(inputtext):
    splittext = inputtext.split(" ")
    tagcount = 0
    for word in splittext:
        if (len(word) > 0):
            for char in word:
                if (char == '<' or char == '>'):
                    tagcount += 1
    return_dict = {'values': [tagcount], 'heads': ['@Attribute html_tag_counts REAL']}
    return return_dict


def not_spammy_words(emailtext):
    spam_words = ['email', 'people', 'time', 'please']
    splittext = emailtext.split(" ")
    total = 0
    for word in spam_words:
        total += splittext.count(word)

    return_dict = {'values': [total], 'heads': ['@Attribute not_spammy_words REAL']}
    return return_dict


def numwords(emailtext):
    splittext = emailtext.split(" ")
    return_dict = {'values': [len(splittext)], 'heads': ['@Attribute numwords REAL']}
    return return_dict

def begin_with_re(emailtext):
    splittext = emailtext.split(" ")
    total = 1
    if ("re" in splittext[0].lower()):
     	total = 0
    return_dict = {'values': [total], 'heads': ['@Attribute begin_with_re REAL']}
    return return_dict
