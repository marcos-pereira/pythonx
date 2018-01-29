# Defining my own exceptions
class MyException(Exception):
    """Basic exception example"""
    # print "My exception was raised"
    pass

class FileIsCorrupted(MyException):
	"""Exception to indicate the file is corrupted"""
	pass

class TryThisException(MyException):
	"""Exception to test raising an arbitrary exception"""
	pass

try:
	f = open('test_file.txt')			# If file name is wrong, IOError exception will happen
	try_exception = False				# If true, the TryThisException will happen, else continue try
	if try_exception:
		raise TryThisException
	if f.name == 'corrupt_file.txt':	# If true, FileIsCorrupted will happen, else continue try
		raise FileIsCorrupted
except IOError as e1:
	print "Sorry, this file does not exist."
	print(e1)
except FileIsCorrupted:
	print "File is corrupted."
except TryThisException:
	print "TryThisException happened"
else:
	print(f.read())
	f.close()
finally:
	print("Executing the finally...")