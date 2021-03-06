#laplacian matrix;
import math 

def adjaceny_mtrx(graph_matrix):
    for i in graph_matrix:
        for j in graph_matrix:
            if(i==j):
                A[i][j] = 0
            else 
                A[i][j] = -1 
    
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

def fnc(i):
    return i*i+2*i+1
    ##implement function

def sq(i):
    return i*i
    
def grad_fn(i,j):
    return weight(i,j)*(fnc(i)-fnc(j))

def smoothness_grph(graph_struct):
    path_sum = []
    for count,v in enumerate(graph_struct):
        path_sum += sq(fnc(v))
        for u in graph_struct:
            if(u!=v):
                path_sum+=wt(u,v)*sq(abs(fnc(u)-fnc(v)))
 
def alpha_strong_convex(y,x,alpha):

def beta_smooth_convex(x,y,beta):

def lipschitz_convex(x,y,lip_coeff):
    
