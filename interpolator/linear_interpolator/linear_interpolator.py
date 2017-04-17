"""
Created on Tue Fev 2017 21:24:35 2017
Last modify on Sun 16 Apr 2017 
@author: marcos-pereira
"""

#-------------------------------------------------------------------------------
# Python short "How to?"
#-------------------------------------------------------------------------------
# this is a comment

# print "Hello World!"

# Example of plotting
#x = [1, 2, 3, 4, 5, 6]
#y = [0.5, 1, 1.5, 2, 2.5, 3]
#print x[0]
#plt.plot(x, y, "ro")
#plt.ylabel('some numbers')
#plt.show()

#-------------------------------------------------------------------------------
# Import libraries
#-------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import sys
plot_all_data = 1; # If equals 1, plot all data


#-------------------------------------------------------------------------------
# Exceptions classes 
#-------------------------------------------------------------------------------
class EmptyFile(RuntimeError):
   def __init__(self, arg):
	  self.args = arg

class e(RuntimeError):
	def __init__(self,arg):
		self.args = arg
		
#-------------------------------------------------------------------------------
# Data file name
#-------------------------------------------------------------------------------
data_file_number = "1";
data_file_name = "test_name";
data_file_extension = ".txt";
data_file = data_file_name + "_" + data_file_number + data_file_extension;

#-------------------------------------------------------------------------------
# User cmd line input arguments
#-------------------------------------------------------------------------------
try:
	print "Reading input parameters...";	
	if (sys.argv[1] is not None) and (sys.argv[2] is not None):		
		print "Input parameters found.";		
		data_file = sys.argv[1];
		print "Data will be read from file " + data_file + ".";
		input_argument_1_interpolation_steps = int(sys.argv[2]);
		print "Number of steps to interpolate is " + sys.argv[2];			
		pass		
except:	
	print "Input parameters are missing!";
	print "Expect 2 input parameters: <arg1: datafile name.txt> <arg2: number of steps to interpolate>.";
	sys.exit(0);
else:
	pass

#-------------------------------------------------------------------------------
# Output data file name including interpolated values
#-------------------------------------------------------------------------------
output_data_file_extension = ".txt";
output_data_file_name = \
data_file_name + \
"_" + data_file_number + \
"_interpolation_result" + \
output_data_file_extension;

#-------------------------------------------------------------------------------
# Read data file and store it into array
#-------------------------------------------------------------------------------
try:	
	print "Opening input data file " + data_file + "...";
	open(data_file) is not None	
except:
	print "File " + data_file + " not found!" + "\n";
	sys.exit(0);
else:
	print "Reading data from input file " + data_file + "...";		
	with open(data_file) as file_holder:
		array = []
		for line in file_holder: # read rest of lines
			array.append([float(data_value) for data_value in line.split()])				
	file_data = [row[0] for row in array]
	file_data_len = len(file_data);
	
try:		
	if len(file_data) > 0:		
		print str(file_data_len) + " values were counted in " + data_file + ".";		
		print "Data from file " + data_file + " read."		
	else:
		raise (EmptyFile("Input data file " + data_file + " is empty!"));
except Exception, empty_data_file:		
	print str(file_data_len) + " values were found in " + data_file + ".";
	print "Input data file " + data_file + " is empty!";		
	sys.exit(0);
# else:			
# 	print "NOT EMPTZ"
# 	#print str(file_data_len) + " values were counted in " + data_file + ".";
# 	print "Data from file " + data_file + " read."
# 	pass	

#-------------------------------------------------------------------------------
# Do linear interpolation
# Reference: https://support.microsoft.com/en-au/help/214096/method-to-calculate-interpolation-step-value-in-excel
#-------------------------------------------------------------------------------
try:	
	if file_data_len != 0: 
		print "Interpolating " + str(input_argument_1_interpolation_steps) + " values between each input value...";				
		pass
except:	
	print "Data file " + data_file + " is empty!";
	sys.exit(0);
else:
	derivative_rate = [];
	interpolated_values = [];
	steps_number_to_add = input_argument_1_interpolation_steps; # Number of steps to be added between each given data value

	#--------------------------------------------------------
	# Calculate derivative rates
	#--------------------------------------------------------
	for ii in xrange(0, file_data_len-1):
		derivative_rate.append((file_data[ii+1] - file_data[ii])/(steps_number_to_add+1));		
	
	#--------------------------------------------------------
	# Calculate interpolated values using the derivative rates
	#--------------------------------------------------------
	for ii in xrange(0, file_data_len-1):
		interpolated_values.append(file_data[ii]);
		print "ii: " + str(ii);
		print "file data " + str(file_data[ii]);
		for jj in xrange(len(interpolated_values)-1, len(interpolated_values)-1+steps_number_to_add):			
			print "interpolated_values " + str(interpolated_values[jj]);
			interpolation_result = interpolated_values[jj]+derivative_rate[ii];
			interpolated_values.append(interpolation_result);
			print "jj: " + str(jj) + ", res: " + str(interpolation_result);		
	if len(file_data) > 0:
		interpolated_values.append(file_data[len(file_data)-1]); # Add the last value	
	print "Interpolation done.";								
	print "Input data:"
	print file_data;
	print "Derivative rates:"
	print derivative_rate;
	print "Linear interpolation result: ";
	print interpolated_values;
	print "Steps added between each initial data: ";
	print steps_number_to_add;	

#-------------------------------------------------------------------------------
# Plot data from file
#-------------------------------------------------------------------------------
try:
	if file_data_len == 0: raise(EmptyFile("Data file " + data_file + " is empty!"));
except:
	print "Data file " + data_file + " is empty!";
	sys.exit(0);
else:	
	print "Plotting input data from file and interpolated values...";		
	plt.plot(interpolated_values, interpolated_values, "bx");
	plt.plot(file_data, file_data, "ro")
	plt.ylabel('yaxis')
	plt.xlabel('xaxis')
	print "Just close the plot window to save the interpolated data to a .txt file..."
	plt.show()	
	

#-------------------------------------------------------------------------------
# Write interpolated data to file
#-------------------------------------------------------------------------------
try:
	output_file_try_create = open(output_data_file_name,'w') is not None;
except Exception, empty_data_file:
	print "Data file " + output_data_file_name + " could not be created!";
	sys.exit(0);
else:	
	print "Creating output file " + output_data_file_name + "... " + str(output_file_try_create) + ".";
	output_file_ = open(output_data_file_name,'w');
	print "Writing data to file" + output_data_file_name + "...";	
	# output_file_.write('interpolated data\n'); # just modify this header as desired
	output_file_.write("\n".join(str(elem) for elem in interpolated_values));
	output_file_.close();
	print "Close file and finish everything."
	