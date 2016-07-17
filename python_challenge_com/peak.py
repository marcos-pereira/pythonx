# http://www.pythonchallenge.com/pc/def/peak.html
# Reference: http://garethrees.org/2007/05/07/python-challenge/

# Look at src page and open the banner

import urllib

def get_challenge(s):
	return urllib.urlopen('http://www.pythonchallenge.com/pc/' + s).read()

banner = get_challenge("def/banner.p")
print banner[0:100]

import pickle

data = pickle.loads(banner)
print data[0:100] # the data seems to be a matrix described by blank spaces and #
print '\n'.join([''.join([p[0] * p[1] for p in row]) for row in data])
