'''
Multiply two matrices together (return -1 if shapes of matrix dont aline), i.e. C = A dot product B
'''
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) != len(b):
        return -1
    
    matrix_results = []
    for i in range(len(a)):
        elements = []
        for j in range(len(b[0])):
            value = 0
            for k in range(len(b)):
                value += a[i][k] * b[k][j]
                           
            elements.append(value)
        matrix_results.append(elements)

    return matrix_results
