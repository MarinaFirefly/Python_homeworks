#addition of slang phrases works with english and russian languages
# -*- coding: utf-8 -*- 
import random 	#for random expressions
import re		#for regular expressions
import sys		#to work with files
import codecs	#for russian language

#open file and read lines from it, get content from all lines
f = codecs.open(sys.argv[1], 'r', 'utf-8') 
line_out = ""
for line in f:
	line_out+=line
f.close()

#get slang phrases as list of strings russian and english differs with codes
slang_phrases_english = [", yeah!", ", this is crazy, I tell ya.", ", can U believe this?", ", eh?", ", aw yea.", ", yo.", "? No way!", ". Awesome!"]
slang_phrases_russian = [", все пучком!", ", держи пятюню!" , ", норм?" ,", зачетно!", ", да не гони."]
slang_phrases = slang_phrases_english if ord(re.findall(r'^.*?\w+',line_out)[0][0]) < 1000 else slang_phrases_russian
#ord(re.findall(r'^.*?\w+',line_out)[0][0]) takes first character of first word and find it's code

#get list of sentences using regular expressions
splited_string = re.split(r'[.!?]',line_out)
splited_string.pop() #last element is always '', so it can be deleted using pop()
#print(splited_string)

#make new setences with slang phrases and write them to other file
f = codecs.open(sys.argv[2], 'w', 'utf-8')
f.write((" ").join([str(x)+random.choice(slang_phrases) for x in splited_string]))
print((" ").join([str(x)+random.choice(slang_phrases) for x in splited_string]))
f.close()