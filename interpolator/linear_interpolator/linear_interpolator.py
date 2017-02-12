"""
Created on Tue Fev 2017 21:24:35 2017
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

plot_all_data = 1; # If equals 1, plot all data


#-------------------------------------------------------------------------------
# Exceptions classes 
#-------------------------------------------------------------------------------
class EmptyFile(RuntimeError):
   def __init__(self, arg):
	  self.args = arg

#-------------------------------------------------------------------------------
# Data file name
#-------------------------------------------------------------------------------
data_file_number = "1";
data_file_name = "test_name";
data_file_extension = ".txt";
data_file = data_file_name + "_" + data_file_number + data_file_extension;

try:
	open(data_file) is not None
except Exception, e:
	print "File " + data_file + " not found!" + "\n";
else:
	#-------------------------------------------------------------------------------
	# Read data file and store into array
	#-------------------------------------------------------------------------------
	with open(data_file) as file_holder:
		array = []
		for line in file_holder: # read rest of lines
			array.append([float(data_value) for data_value in line.split()])				
	file_data = [row[0] for row in array]
	file_data_len = len(file_data);

#-------------------------------------------------------------------------------
# Do linear interpolation
#-------------------------------------------------------------------------------
try:
    if file_data_len == 0: raise(EmptyFile("Data file " + data_file + " is empty!"));
except Exception, empty_data_file:
    print "Data file " + data_file + " is empty!";
else:
    derivative_rate = [];
    interpolated_values = [];
    steps_number_to_add = 2;
    for ii in xrange(1, file_data_len-1):
        derivative_rate.append((file_data[ii+1] - file_data[ii])/(steps_number_to_add+1));        
        print derivative_rate;

    # for jj in xrange(1, steps_number_to_add):            
    #     interpolated_values.append(file_data[ii]+derivative_rate[jj]);        

#-------------------------------------------------------------------------------
# Plot data from file
#-------------------------------------------------------------------------------
try:
	if file_data_len == 0: raise(EmptyFile("Data file " + data_file + " is empty!"));
except Exception, empty_data_file:
	print "Data file " + data_file + " is empty!";
else:	
	print "Ploting data from file...";	
	# plt.subplot(3,1,1)
	plt.plot(file_data, file_data, "ro")
	plt.ylabel('yaxis')
	plt.xlabel('xaxis')
	plt.show()