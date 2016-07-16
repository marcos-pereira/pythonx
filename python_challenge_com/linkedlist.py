# initial_page = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"

# This solution was adapted from: http://garethrees.org/2007/05/07/python-challenge/

import urllib
import re

# Be patient and somewhen you will reach it!
initial_page = 12345 # until it doesnt work anymore, then get the last working number
# initial_page = 94485 # than divide by two and keep going
# initial_page = 25357 # you may reach this number
# initial_page = 63579 # if you loose yourself choose take this way

def next_page(p):
   text = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?'
                         'nothing=%s' % p).read()
   m = re.match('and the next nothing is ([0-9]+)', text)
   # m = re.match('next nothing is ([0-9]+)', text)
   if not m: 
   		print text   
   print m.group(1)
   return m.group(1)   		
   # elif m.group(1)==16044:
   # 		return m.group(1)
   # else:		

result = initial_page
i = 0
while (result):
	print i
	i = i + 1	
	result = next_page(result)   		
	if not result:
		print result	
	if result == 16044:
		result = result/2
	else:
		print result
		

   