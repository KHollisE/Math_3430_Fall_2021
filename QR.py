import LA


#Problem 2 for HW06
def Q(matrix_A: list)->list:
    """
    Gives an orthonormal list of vectors 
    
    Sets three parameters as empty sets and R parameter as a
    matrix of zero vectors. Creates a for loop to get an R value that solves
    for Q. Then using the value of matrix input with the inner product of 
    matrix_B and Q we solve for R. Returns Q.
    
    Args:
        matrix_A: A matrix stored as a list.
    Returns:
        Q: An orthonormal matrix stored as a list
    """
    Q: list = []
    matrix_B = []
    R: list = [[0 for element in range(len(matrix_A[0]))] for index in range(len(matrix_A))]
    for x in matrix_A:
        matrix_B.append(x)
    for y in range(len(matrix_A)):
        R[y][y] = LA.boolean_norm(matrix_B[y])
        Q.append(LA.scalar_vector_mult(1/R[y][y], matrix_B[y]))
        for z in range(y, len(matrix_A)):
            R[z][y] = LA.inner_product(Q[y], matrix_B[z])
            matrix_B[z] = LA.add_vectors(matrix_B[z], LA.scalar_vector_mult(-R[z][y], Q[y]))
    return Q 


def stable_gram(matrix_A: list)->list:
    """
    Gives the Q and R factorization using Stable Gram Schmidt
    
    Sets three parameters as empty sets and R parameter as a
    matrix of zero vectors. Creates a for loop to get an R value that solves
    for Q. Then using the value of matrix input with the inner product of 
    matrix_B and Q we solve for R. Returns both Q and R.
    
    Args:
        matrix_A: A matrix stored as a list.
    Returns:
        The Q and R factorization.
    """
   
    Q: list = []
    matrix_B = []
    R: list = [[0 for element in range(len(matrix_A[0]))] for index in range(len(matrix_A))]
    for x in matrix_A:
        matrix_B.append(x)
    for y in range(len(matrix_A)):
        R[y][y] = LA.boolean_norm(matrix_B[y])
        Q.append(LA.scalar_vector_mult(1/R[y][y], matrix_B[y]))
        for z in range(y, len(matrix_A)):
            R[z][y] = LA.inner_product(Q[y], matrix_B[z])
            matrix_B[z] = LA.add_vectors(matrix_B[z], LA.scalar_vector_mult(-R[z][y], Q[y]))
    return Q,R
    
print(Q([[1,-1,1],[1,0,1],[1,1,2]]))
print(Q([[2,-1,1],[1,0,3],[1,4,2]]))

print(stable_gram([[1,-1,1],[1,0,1],[1,1,2]]))
print(stable_gram([[2,-1,1],[1,0,3],[1,4,2]]))















