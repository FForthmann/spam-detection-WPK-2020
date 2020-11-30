import csv

import numpy as np


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
    with open('spammy_words_list.csv', newline='') as f:
        reader = csv.reader(f)
        spam_words = list(reader)

    spam_words = np.array(spam_words)
    spam_words = spam_words.flatten()

    inputtext = inputtext.lower()
    splittext = inputtext.split(" ")
    total = 0
    for word in spam_words:
        total += splittext.count(word)

    total_spammy_words = total / len(splittext)

    return_dict = {'values': [total_spammy_words], 'heads': ['@Attribute spammy_words REAL']}
    return return_dict


def spammy_phrases(inputtext):
    with open('spammy_words_list_internet.csv', newline='') as f:
        reader = csv.reader(f)
        spam_words = list(reader)

    spam_words = np.array(spam_words)
    spam_words = spam_words.flatten()
    inputtext = inputtext.lower()

    total = 0
    for word in spam_words:
        word = word.lower()

        if (word in inputtext):
            total += 1

    total_spammy_words = total

    return_dict = {'values': [total_spammy_words], 'heads': ['@Attribute spammy_phrases REAL']}
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


def square_bracket_count(inputtext):
    splittext = inputtext.split(" ")
    tagcount = 0
    for word in splittext:
        if (len(word) > 0):
            for char in word:
                if (char == '[' or char == ']'):
                    tagcount += 1
    return_dict = {'values': [tagcount], 'heads': ['@Attribute square_bracket_tag_counts REAL']}
    return return_dict


def has_exclamation_mark(emailtext):
    splittext = emailtext.split(" ")
    total = 0
    for word in splittext:
        if ("!" in word):
            total += 1
    return_dict = {'values': [total], 'heads': ['@Attribute has_exclamation_mark REAL']}
    return return_dict


def has_html(emailtext):
    solution = 1 if "html" in emailtext.lower() else 0
    return_dict = {'values': [solution], 'heads': ['@Attribute has_html REAL']}
    return return_dict


def num_link(emailtext):
    solution = emailtext.count('http')
    return_dict = {'values': [solution], 'heads': ['@Attribute num_link REAL']}
    return return_dict


def has_gifs(emailtext):
    solution = 1 if ".gif" in emailtext.lower() else 0
    return_dict = {'values': [solution], 'heads': ['@Attribute has_gifs REAL']}
    return return_dict


def has_jpg(emailtext):
    solution = 1 if ".jpg" in emailtext.lower() else 0
    return_dict = {'values': [solution], 'heads': ['@Attribute has_jpgs REAL']}
    return return_dict


def grossbuchstaben(inputtext):
    splittext = inputtext.split(" ")
    tagcount = 0
    for word in splittext:
        if (len(word) > 0):
            for char in word:
                if (char.isupper()):
                    tagcount += 1
    return_dict = {'values': [tagcount], 'heads': ['@Attribute grossbuchstaben REAL']}
    return return_dict


def words_containing_numbers_ratio(inputtext):
    splittext = inputtext.split(" ")
    total = 0
    for word in splittext:
        if any(char.isdigit() for char in word):
            total += 1
    amount_words = float(len(splittext))
    return_dict = {'values': [total / amount_words], 'heads': ['@Attribute words_containing_numbers_ratio REAL']}
    return return_dict


def day_of_week(inputtext):
    splittext = inputtext.split(" ")
    day = 0
    for word in splittext:
        if (word == "Mon"):
            day = 1
        elif (word == "Tue"):
            day = 2
        elif (word == "Wed"):
            day = 3
        elif (word == "Thu"):
            day = 4
        elif (word == "Fri"):
            day = 5
        elif (word == "Sat"):
            day = 6
        elif (word == "Sun"):
            day = 7
    return_dict = {'values': [day], 'heads': ['@Attribute day_of_week REAL']}
    return return_dict
