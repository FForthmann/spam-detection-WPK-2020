import csv

def amount_cap_words(inputtext):
	splittext = inputtext.split(" ")
	total = 0
	first = ""
	for word in splittext:
		if (len(word) > 0):
			first = word[0]
			if first.isupper():
				total += 1
	return_dict = {'values' : [total], 'heads' : ['@Attribute amount_cap_words REAL']}
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
	
	return_dict = {'values' : [total_cap_words/amount_words], 'heads' : ['@Attribute cap_word_ratio REAL']}
	return return_dict

def spammy_words(inputtext):
	with open('spammy_words_list.csv', newline='') as f:
		reader = csv.reader(f)
		spam_words = list(reader)

	splittext = inputtext.split(" ")
	total = 0
	for word in spam_words:
		total += splittext.count(word)
		
	total_spammy_words = float(total)
	
	return_dict = {'values' : [total], 'heads' : ['@Attribute spammy_words REAL']}
	return return_dict
