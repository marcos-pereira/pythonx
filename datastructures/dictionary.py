#!/usr/bin/env python2.7

# Source: https://docs.python.org/2/tutorial/datastructures.html

# Create dictionary
code_key = {'a':1, 'b':2, 'c':3};
print "a = " + str(code_key['a']);
print "b = " + str(code_key['b']);
print "c = " + str(code_key['c']);

# Delete key:value pair and add new one
del code_key['b'];
code_key['d'] = "rty";
print code_key.keys();
print code_key;

# Print unsorted code keys
code_key = {'a':"qwe", 'b':"asd", 'c':"zxc"};
print "a = " + str(code_key['a']);
print "b = " + str(code_key['b']);
print "c = " + str(code_key['c']);
print "code_key keys: " + str(code_key.keys());

# Sort code keys
sorted_keys = sorted(code_key);
print str(sorted_keys);

# Check if key in dictionary
print "Is b in dictionary?";
print 'b' in code_key;




