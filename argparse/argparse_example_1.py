#!/usr/bin/python
import argparse
import sys

def do_stuff():
	print "Doing my stuff..."

# The parse arguments function could also be defined in an external file
# The external file could be imported and the parse argument function be called
# external_file.parseArguments()
def parse_arguments():
	parser = argparse.ArgumentParser(description='This parser parse the user input arguments')	# Create an argument parser object
	
	# Take strings in cmd line and turn into objects which have the argument type as attribute 
	parser.add_argument('-i','--input', help='Input file name',required=True)		
	parser.add_argument('-o','--output',help='Output file name', required=True)		
	parser.add_argument('-s','--superuser', help='Superuser name', required=False)	
	parser.add_argument('--version',help='Program version', required=False)			
	parser.add_argument('-v','--verbose', help='Verbose', required=False)	
			
	args = parser.parse_args()	# Automatically determine the command line arguments from sys.argv
	 
	## show values ##
	# print ("Input file: %s" % args.input )
	# print ("Output file: %s" % args.output )
	# print ("Superuser: %s" %args.superuser)
	# print ("Version: %s" %args.version)
	# print ("Verbose: %s" %args.verbose)

	return args

def main(args):
	print ("Input file: %s" % args.input )
	print ("Output file: %s" % args.output )
	print ("Superuser: %s" %args.superuser)
	print ("Version: %s" %args.version)
	print ("Verbose: %s" %args.verbose)
	
	do_stuff()

if __name__ == "__main__":
	arguments = parse_arguments()
	main(arguments)
	sys.exit()