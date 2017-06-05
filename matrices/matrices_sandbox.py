"""
Created on Mon 16th Apr 2017 13:01:35 2017
Last modify Mon 5th Jun 2017
@author: marcos-pereira
"""

#-------------------------------------------------------------------------------
# Import libraries
#-------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import sys
import math as math

#-------------------------------------------------------------------------------
# Declare matrices to test
#-------------------------------------------------------------------------------
A = np.matrix( [[1, 2, 3], [4, 5, 6], [7, 8, 9]] );
x = np.matrix( [[1], [2], [3]] );
y = np.matrix( [[1, 2, 3]] );
identity_matrix = np.eye(3); # 3x3 identity matrix
moore_penrose_example = np.matrix( [[1, 1, 1], [2, 2, 2], [1, 1, 1], [2, 2, 2]]);
eig_vector_example = np.array([[0.0, -1.0], [1.0, 0.0]]);

#-------------------------------------------------------------------------------
# Test basic matrices operations
# Reference: https://docs.scipy.org/doc/numpy-dev/user/quickstart.html#linear-algebra
#-------------------------------------------------------------------------------
print "A:";
print A; # Transpose

print "Transpose of A:";
print A.T; # Transpose

print "Multiplication of A bz x";
print A*x; # Multiplication

print "Inverse of A";
print A.I; # Inverse

print "Solve linear system for y Ay=x";
print np.linalg.solve(A, x); # Solve linear 

print "Identity matrix 3x3";
print identity_matrix; # Identity matrix

print "Identity matrix x3";
print 3*identity_matrix; # identity matrix multiplied by 3

print "Trace of identity matrix";
print np.trace(1*identity_matrix); # trace of identity matrix = sum of the elements on the main diagonal(the diagonal from the upper left to the lower right) 

print "Trace of identity matrix x3";
print np.trace(3*identity_matrix);

print "Eigen vectors of eig_vector_example";
print np.linalg.eig(eig_vector_example);

print "Moore Penrose Pseudoinverse of moore_penrose_example"
print np.linalg.pinv(moore_penrose_example);


#-------------------------------------------------------------------------------
# EXAMPLE 1 
# Test to do a least squares minimization and obtain the linear model of a system given inputs and outputs
#-------------------------------------------------------------------------------
# i = a1u+a2u^2+a3u^3
# u = [0.06 0.1 0.2 0.3 0.4 0.45]
# i = [1 0.85 0.25 0.1 0.25 0.6]

# Pseudoinverse in least squares
# A x = b
# x0 = pinv(A)*b = transpose([a1 a2 a3])
# i = b = [1 0.85 0.25 0.1 0.25 0.6]
# i = a1u+a2u^2+a3u^3 = [u u^2 u^3]transpose([a1 a2 a3])
# i = b = A x
# A = [u u^2 u^3] with dimensions sizeof(u) rows and three rows, that is, u, u^2 and u^3
# We want to find then x = pinv(A)*b = pinv(A)*i, where i is a column vector with sizeof(i)
# Moore Penrose pseudo inverse solution
# pinv(A) = inv((transpose(A)*A)) * transpose(A)

# Create matrix A
u_input = np.matrix( [[0.06, 0.1, 0.2, 0.3, 0.4, 0.45]] );
print "u_input:";
print u_input;

u_input_2 = np.asarray(u_input)**2;
print "u_input^2";
print u_input_2;

u_input_3 = np.asarray(u_input)**3;
print "u_input^3";
print u_input_3;

# Reference for concatenation: https://docs.scipy.org/doc/numpy/reference/generated/numpy.concatenate.html
A_matrix = np.concatenate((u_input,u_input_2,u_input_3),axis=0).T; # A_matrix will be a three column matrix, therefore the transpose
print "A_matrix";
print A_matrix;

# Print system output
i_output = np.matrix( [[1, 0.85, 0.25, 0.1, 0.25, 0.6]] );
print "i_output:";
print i_output;

# Calculate the pseudo inverse
A_pinv = (A_matrix.T*A_matrix)
A_pinv = A_pinv.I * A_matrix.T;	# Calculate pinv using math formula
# A_pinv = np.linalg.pinv(A_matrix); # Calculate pinv using python function
print "A_pinv:";
print A_pinv;

# Calculate x0=A_pinv*b=A_pinv*i using pseudo inverse
x0 = A_pinv*i_output.T; # use transpose(i_output) because i_output is a row vector
print "x0:";
print x0;

# Calculate i = A*x0
A_x0 = A_matrix*x0;
print "A x0 =";
print A_x0;

# Calculate estimation error for each point
estimation_error = i_output.T - A_x0;
print "estimation_error = i_output.T - A_x0:";
print estimation_error;

# Calculate estimation squared error norm
squared_error_norm = np.asarray(i_output.T - A_x0)**2;
squared_error_norm = np.linalg.norm(squared_error_norm, ord = 2); # Ref: https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.norm.html
print "squared_error_norm:";
print squared_error_norm;

# Plot given data
print "Plotting input data for i";		
plt.plot(i_output, u_input, "bx");
# Plot estimated data
plt.plot(A_x0.T, u_input, "ro"); # use transpose(A_x0) because it was a column vector
plt.ylabel('i');
plt.xlabel('u');
# TODO: implement save_to_file
# print "Just close the plot window to save the interpolated data to a .txt file...";
plt.show();