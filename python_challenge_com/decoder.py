#!/usr/bin/python

message_1 = "This is message 1."

message_to_decode = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "


# Decoding loop: letter + 2 positions
# ex: 
# a + 2 positions = c
# b + 2 positions = d and so it goes on
for ii in xrange(0, len(message_1)):
	# print message_1[ii]
	print chr(ord(message_to_decode[ii])+2),
