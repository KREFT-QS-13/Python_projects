from scipy import *
import numpy as np
from numpy import linalg as la

def eigenvalue(A):
    # eigenvalues X of matrix 2x2 [[a,b] , [c,d]] are roots of quadratic equation: (a-X)*(d-X)-bc = 0
    return (  0.5*(A[0][0]+A[1][1]+sqrt((A[0][0]+A[1][1])**2-4*A[0][0]*A[1][1]+4*A[0][1]*A[1][0])), 0.5*(A[0][0]+A[1][1]-sqrt((A[0][0]+A[1][1])**2-4*A[0][0]*A[1][1]+4*A[0][1]*A[1][0])) )

A = np.random.randint(low=1,high=50,size=(2,2))
# A = array([[5,3],[-6,-4]])
# A = array([[1,-1],[1, 1]])
print(A)
e1, e2 = eigenvalue(A)
print("Eigenvalues of A (method 1): {:.3f}, {:.3f}".format(e1,e2))
w, vec = la.eig(A)
print("Eigenvalues of A (method 2): {:.3f}, {:.3f}".format(w[1],w[0]))