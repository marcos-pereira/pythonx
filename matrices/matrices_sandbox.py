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
from collections import OrderedDict # Needed to remove repeated labels on plots

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
print "Plotting i and estimated points";		
plt.plot(i_output, u_input, "ro", markersize = 5, label = 'i');
# Plot estimated data
plt.plot(A_x0.T, u_input, "bx", markersize = 10, label = 'i estimated'); # use transpose(A_x0) because it was a column vector
plt.ylabel('i');
plt.xlabel('u');
# Remove repeated labels
handles, labels = plt.gca().get_legend_handles_labels();
by_label = OrderedDict(zip(labels, handles));
plt.legend(by_label.values(), by_label.keys(), loc = 'best', numpoints = 1);
plt.grid(True);
# TODO: implement save_to_file
# print "Just close the plot window to save the interpolated data to a .txt file...";
plt.show();

#-------------------------------------------------------------------------------
# EXAMPLE 2
# Test to do a least squares minimization and obtain the linear model of a system given inputs and outputs
#-------------------------------------------------------------------------------
# U = b + (1/L)*a, the parameters to estimate are a and b, L is the input variable
# L = [10 20 30 40 50 60 70 80]
# U = [2.4 1.4 1.0 0.75 0.6 0.55 0.5 0.4]

# L_inputs
L_input = np.matrix( [[10, 20, 30, 40, 50, 60, 70, 80]] );
print "L_input:";
print L_input;

# Calculate 1/L
L_input_inverse = np.asarray(L_input)**-1.0;
print "L_input_inverse";
print L_input_inverse;

# Create column of ones
ones_vector = np.ones(8);
ones_vector = np.matrix(ones_vector);
print "ones_vector:";
print ones_vector;

# Create A_matrix_2
A_matrix_2 = np.concatenate((ones_vector,L_input_inverse), axis=0).T; # The transpose is used because the A_matrix should be a two column matrix
print "A_matrix_2:";
print A_matrix_2;

# Print system output U
U_output = np.matrix( [[2.4, 1.4, 1.0, 0.75, 0.6, 0.55, 0.5, 0.4]] );
print "U_output:";
print U_output;

# Calculate the pseudo inverse of A
A_2_pinv = (A_matrix_2.T * A_matrix_2).I * A_matrix_2.T
print "A_2_pinv:";
print A_2_pinv;

# Calculate x0 = pinv(A) * b = pinv(A) * U
x0_2 = A_2_pinv * U_output.T;
print "x0_2:";
print x0_2;

# Calculate A_matrix_2*x0_2 = b = U 
A_x0_2 = A_matrix_2 * x0_2;
print "A_x0_2:";
print A_x0_2;

# Calculate estimation error for each point
estimation_error_2 = U_output.T - A_x0_2;
print "estimation_error = U_output.T - A_x0_2:";
print estimation_error;

# Calculate estimation squared error norm
squared_error_norm_2 = np.asarray(U_output.T - A_x0_2)**2;
squared_error_norm_2 = np.linalg.norm(squared_error_norm_2, ord = 2); # Ref: https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.norm.html
print "squared_error_norm_2:";
print squared_error_norm_2;

# Plot given data
print "Plotting U and estimated points";		
plt.plot(U_output, L_input, "ro", markersize = 5, label = 'U');
# Plot estimated data
plt.plot(A_x0_2.T, L_input, "bx", markersize = 10, label = 'U estimated'); # use transpose(A_x0) because it was a column vector
plt.ylabel('U');
plt.xlabel('L');
# Remove repeated labels
handles, labels = plt.gca().get_legend_handles_labels();
by_label = OrderedDict(zip(labels, handles));
plt.legend(by_label.values(), by_label.keys(), loc = 'best', numpoints = 1);
plt.grid(True);
# TODO: implement save_to_file
# print "Just close the plot window to save the interpolated data to a .txt file...";
plt.show();

