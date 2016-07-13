#!/usr/bin/python
import string

message_1 = "This is message 1."

message_to_decode_1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb."
message_to_decode_2 = "rfyrq ufyr amknsrcpq ypc dmp."
message_to_decode_3 = "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle."
message_to_decode_4 = "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb."
message_to_decode_5 = "lmu ynnjw ml rfc spj."

message_to_decode = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url_message = "http://www.pythonchallenge.com/pc/def/map.html"
message_to_decode = url_message

# Decoding loop: letter + 2 positions
# ex: 
# a + 2 positions = c
# b + 2 positions = d and so it goes on

# Alphabet
alphabet = ""
for ii in xrange(97,97+26):
	alphabet += chr(ii)

# Encoded alphabet
code = ""
for ii in xrange(97,97+26):
	code += chr(ii+2)

print("Alphabet: ", alphabet)
print("Alpha Code: ", code)

# Code lookup table
decoder = string.maketrans(alphabet, code)

# Decode string
decoded_message = message_to_decode.translate(decoder)

print("Coded message: ", message_to_decode)
print("Decoded message: ", decoded_message)

# for ii in xrange(0, len(message_1)):
# 	# print message_1[ii]
# 	print chr(ord(u,message_to_decode_1[ii])+2),
# print 

# for ii in xrange(0, len(message_1)):
# 	# print message_1[ii]	
# 	print chr(ord(message_to_decode_2[ii])+2),
# print

# for ii in xrange(0, len(message_1)):
# 	# print message_1[ii]	
# 	print chr(ord(message_to_decode_3[ii])+2),
# print

# for ii in xrange(0, len(message_1)):
# 	# print message_1[ii]	
# 	print chr(ord(message_to_decode_4[ii])+2),
# print

# for ii in xrange(0, len(message_1)):
# 	# print message_1[ii]	
# 	print chr(ord(message_to_decode_5[ii])+2),		
# print



# See: http://www.dotnetperls.com/ord-python