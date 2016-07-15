#!/usr/bin/python

# from collections import Counter

# import re

# code = open("rare_characters.txt")

# code_key = ['#','@','!','$','%','+','{','}','[',']','_','-','&','*','(',')','*','^','@','/']
# decoded_output =""

# # print()
# # for letter in code:
# #     if letter not in code_key:
# #         decoded_output += letter
# #         print letter       


# # count = Counter(code)
# # s = ''.join(char for char in code if count[char] < 10)
# # print(s)        

# # decoded_output.strip()

# # print(decoded_output)

# # characters = Counter(code)
# # print(characters.most_common())

# # message = re.findall("[a-zA-Z]", code)
# # print message


# Solution Reference Level 2: http://garethrees.org/2007/05/07/python-challenge/
import urllib
def get_challenge(s):
     return urllib.urlopen('http://www.pythonchallenge.com/pc/' + s).read()
src = get_challenge('def/ocr.html')
import re
text = re.compile('<!--((?:[^-]+|-[^-]|--[^>])*)-->', re.S).findall(src)[-1]
counts = {}
for c in text: counts[c] = counts.get(c, 0) + 1
counts
print ''.join(re.findall('[a-z]', text))

# Level 3

src = get_challenge('def/equality.html')
text = ''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',src))
print text
