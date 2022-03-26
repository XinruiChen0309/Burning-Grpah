import numpy as np
import numpy.linalg as la
import copy as cp
from random import seed
from random import random

'''
P1 random adj matrix generator
input:
    dim: dimension of the matrix
output:
    A: adj matrix with the given dimension
'''
def generate_random_matrix(dim):
    N = dim
    A = np.zeros([N,N])#create 0 matrix
    # fill value
    for i in range(N):
        for j in range(i + 1, N):
            # use random to generate random graph
            tem = random()
            if (tem < 0.4):
                A[i][j] = 1
                A[j][i] = 1
    return A

def get_B(T, num_round):
    A = cp.deepcopy(T) # for  matrix
    B = cp.deepcopy(T) # final matrix
    # produce B
    for i in range(2, num_round + 1):
        A = A @ T  # T1^l
        B = B + A  # B =  T1 + T1^2 + ... + T1^l
    return B

'''
P2: is_burned detector
input: 
  T is test matrix
  number of sources
  number of rounds
output:
  boolean: whether the graph can be burned with num_source sources which will all burn num_round rounds
'''
def is_burned(T, num_source, num_round):
    # S1: get B
    B = get_B(T, num_round)
    de = 0
    # S2: burn the graph
    
    while num_source > 0:
        if de == 1:
            B = get_B(B, num_round)
        de = 1
        N = B.shape[0]
        
        # 2.1 case1: burned before running out of sources
        if N == 0 or N == 1:
            return True
        
        # 2.2 mark the row which contains most non-zero indexs
        max_idx = -1
        max = 0  
        
        # 2.2+ walk through the rows to find max
        for j in range(N):
           if np.count_nonzero(B[j]) > max:
               max = np.count_nonzero(B[j])
               max_idx = j
        
        # 2.3 delete the rows and cols
        
        # 2.3.1 mark the row and col need to be delete and reverse 
        # in case that out of index
        to_delete = []
        for k in range(N):
            if B[max_idx][k] != 0:
                to_delete.append(k)
        to_delete.reverse()
        print(to_delete)
 
        # 2.3.2 delete the row and columns
        for k in range(len(to_delete)):
            print(B)
            B = np.delete(B, to_delete[k], 0)
            B = np.delete(B, to_delete[k], 1)
                
        
        num_source = num_source - 1 #update sources 
        num_round = num_round - 1 #update rounds comment this line if each source burn for k rounds
        print(max_idx, max, B)
    #case2: the graph being burned at last round
    return (B.shape[0] == 0)

# Work space
A_dimension = 4
source = 2
round = 1
T1 = generate_random_matrix(A_dimension)
print("test matrix is \n", T1)
T2 = np.array([
    [0, 0, 1, 0,],
    [0, 0, 0, 1,],
    [1, 0, 0, 0,],
    [0, 1, 0, 0,]])
print(is_burned(T2, source, round))
            
            
        
    

