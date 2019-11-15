#find number of the words in the text and print them as a set
import random 	#for random expressions
import re		#for regular expressions
import sys		#to work with files

#open file and read lines from it, get content from all lines
f = open(sys.argv[1],'r')
line_out = ('').join(line for line in f)
f.close()

# function deletes last char (dividor) from end and makes all words in lowercase
def change_word(word):
	return word[:-1].lower() 

list_of_words = list(map(change_word,re.findall(r'\w+\W',line_out))) # find words with some dividor

def cnt_word(word):
	cnt = list_of_words.count(word)
	return word + ': ' + str(cnt)

print(set(map(cnt_word, list_of_words)))