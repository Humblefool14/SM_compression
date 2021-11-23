#laplacian matrix;
import math 

def L(u,v):
    if(u == v):
        return diag(u)
    if(connected(u,v)):
        return -1
    else return 0

def L_normalized(u,v):
    if(u==v):
        return 1
    if(connected(u,v)):
        return 1/math.sqrt(diag(u)*diag(v))
    else return 0

