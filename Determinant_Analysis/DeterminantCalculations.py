# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 14:31:02 2016

@author: mct00
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math



###-------------------------------------------------------------------------------
###
### Given any pair of nxn matrices A and B, I'd like to randomly generate orthogonal
### matrics U, X, Y, and Z and investigate the determinants of matrices of the form
### UAX + YBZ. This program uses pandas and NumPy to generate a large number of 
### matrices of this form (for fixed A and B). Determinants of the matrices, as well
### as all of the relevent matrices, are stores in text files.
###
###-------------------------------------------------------------------------------






### Choose the size of the matrices.
n = 20




### Calculate singular values of A and B.
def svals(x):
    y = []
    for i in range(n):
        y.append(math.sqrt(np.linalg.eig(np.transpose(np.mat(x))*np.mat(x))[0][i]))
    y.sort()
    return y
 
### Find scaling factor for A+B.       
def radius(x,y,n):
    p = 1
    for i in range(n):
        p = p*(svals(x)[i]+svals(y)[n-i-1])
    return p

### Create scaled A and B.
def normalize(x,y,n):
    return [1/(radius(x,y,n))**(1/n)*x, 1/(radius(x,y,n))**(1/n)*y]

### Find the orthogonal component of a matrix in its QR factorization.
def orthogonalize(x):
    return np.linalg.qr(x)[0]




### Procedure for making the desired calculations.
def data(a,b,c,d,e,f,n):
    sm = np.matrix(orthogonalize(a))*normalize(e,f,n)[0]*np.matrix(orthogonalize(b))+np.matrix(orthogonalize(c))*normalize(e,f,n)[1]*np.matrix(orthogonalize(d))
    return [sm, np.linalg.det(sm)*10**34]

### Fix A and B, randomly generate 1000 quadruples W, X, Y, Z of orthogonal matrices; returns the determinant
### of the matrix WAX+YBZ.
def genData():
    
    ### Generate A and B to be used throughout process; normalize to a and b.
    m1 = pd.DataFrame(np.random.randn(n,n))
    m2 = pd.DataFrame(np.random.randn(n,n))
    a = normalize(m1,m2,n)[0]
    b = normalize(m1,m2,n)[1]
    
    detList = {}

    for i in range(1000):
        o1 = pd.DataFrame(np.random.randn(n,n))
        o2 = pd.DataFrame(np.random.randn(n,n))
        o3 = pd.DataFrame(np.random.randn(n,n))
        o4 = pd.DataFrame(np.random.randn(n,n))
        detList[i] = data(o1,o2,o3,o4,a,b,n)[1]
    return detList     
      
        