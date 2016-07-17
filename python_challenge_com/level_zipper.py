# Reference: http://garethrees.org/2007/05/07/python-challenge/

import zipfile
import urllib
import StringIO
import re

def get_challenge(s):
	return urllib.urlopen('http://www.pythonchallenge.com/pc/' + s).read()

def get_file(p):
	text = z.read('%s.txt' % p)
	m = re.match('Next nothing is ([0-9]+)', text)
	if not m: 
   		print text   
   	return m.group(1)  

# z = zipfile.ZipFile(StringIO.StringIO(get_challenge('def/channel.zip')))
z = zipfile.ZipFile(StringIO.StringIO(get_challenge('def/channel.zip')),'r') # look out not to name no file in the folder as zipfile.py
print z.namelist()
print len(z.namelist())

# The last file on the zipfile list is a readme.txt

print z.read('readme.txt') # point to 90052
print z.read('90052.txt') # point to 94191

# collect comments


zipp = []
result = 90052
# while result:	
# 	zipp.append(result)
# 	result = get_file(result)	
# 	if not result:
# 		print result
# 	else:
# 		print result

for i in range(len(z.namelist())):
	zipp.append(result)
	result = get_file(result)
# If you run until here, the script will raise an error

# Enter the Python Terminal environment and run this whole script
# If you run on the python terminal environment, the variable zipp will still exist and you will be able to print it

print ''.join([z.getinfo('%s.txt' % p).comment for p in zipp])




