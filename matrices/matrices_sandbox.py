"""
Created on Mon 16th Apr 2017 13:01:35 2017
Last modify Mon 16th Apr 2017
@author: marcos-pereira
"""

#-------------------------------------------------------------------------------
# Import libraries
#-------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import sys

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