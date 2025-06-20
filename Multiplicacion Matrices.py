from collections import defaultdict
def pretty_print(mat):
    for row in mat:
        print(row)

def multiply(a,b):
    if len(a[0])!=len(b):
        print("Matrices Inválidas")
        return
    result = []
    for iY in range(len(a)):
        result.append([])
        for iX in range(len(b[0])):
            result[iY].append(0)
            for c in range(len(a[0])):
                result[iY][iX] += a[iY][c]*b[c][iX]
    return result



a = [
    [1,0],
    [0,-2]
]
b = [
    [2,0,0,0],
    [0,3,0,0],
    [0,0,-4,0],
    [0,0,0,5]
]
pretty_print(a)
print()
pretty_print(multiply(a,b))
