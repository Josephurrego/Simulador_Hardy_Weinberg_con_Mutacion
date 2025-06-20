import numpy as np

def pretty_print(mat):
    for i in mat:
        print(i)

def identityMat(n):
    return [[1 if i==x else 0 for i in range(n)] for x in range(n)]

def LU(mat:list[list[int]]):
    U = mat.copy()
    L = identityMat(len(mat))
    for col in range(len(mat)):
        for row in range(len(mat)-col-1):
            operationalRow = mat[col]
            if operationalRow[col]==0:
                continue
            constantEl = -(mat[row+col+1][col]) / operationalRow[col]
            L[row+col+1][col] = -(constantEl) # Save L, operation
            for idx,el in enumerate(mat[row+col+1]):
                U[row+col+1][idx] = el+(constantEl*mat[col][idx])
    return np.array(L),np.array(U)

def findValues(A:np.ndarray,B:np.ndarray,backwards:bool=False):
    A = A.copy()
    X = np.zeros(len(B))
    
    for idx in range(len(B)):
        if backwards:
            X[len(B)-1-idx] = (B[len(B)-1-idx]-sum(A[len(B)-1-idx][len(B)-1-x]*X[len(B)-1-x] for x in range(idx)))/A[len(B)-1-idx][len(B)-1-idx]
        else:
            X[idx] = (B[idx]-sum(A[idx][x]*X[x] for x in range(idx)))/A[idx][idx]

    return X

def solveByLU(A,B):
    B = np.array(B)
    La,Ua = LU(A)
    y = findValues(La,B)
    x = findValues(Ua,y,True)
    return x
    

mat_A = [
    [2,1,0,0,0], # Desde A1
    [4,3,1,0,0], # Desde A2
    [0,2,3,1,0], # Desde A3
    [0,0,1,4,2], # Desde A3
    [0,0,0,1,5]  # Desde A4
]
mat_B = [1,4,10,18,19]
print(solveByLU(mat_A,mat_B))

