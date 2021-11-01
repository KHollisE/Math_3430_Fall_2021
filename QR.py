import LA


def unstable_gram(matrix_A: list)->list:
    """
    Gives the Q and R factorization using Unstable Gram Schmidt
    
    Sets three parameters as matrices of zero vectors. Creates a for loop to 
    give R a value as the inner product of matrix_B and Q. Gives a new value of 
    matrix_B through the add_vectors funciton from LA.py. Solves for Q and R.
    
    Args:
        matrix_A: A matrix stored as a list.
    Returns:
        The Q and R factorization.
    """
    Q: list = [[0 for element in range(len(matrix_A[0]))] for index in range(len(matrix_A))]
    matrix_B = [[0 for element in range(len(matrix_A[0]))] for index in range(len(matrix_A))]
    R: list = [[0 for element in range(len(matrix_A[0]))] for index in range(len(matrix_A))]
    for x in range(len(matrix_A)):
        matrix_B[x] = matrix_A[x]
        for y in range(x):
            R[x][y] = LA.inner_product(matrix_B[x], Q[y])
            matrix_B[x] = LA.add_vectors(matrix_B[x], LA.scalar_vector_mult(-R[x][y], Q[y]))
        R[x][x] = LA.boolean_norm(matrix_B[x])
        Q[x] = LA.scalar_vector_mult(1/R[x][x], matrix_B[x])
        
    return Q, R


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
    
print(unstable_gram([[1,-1,1],[1,0,1],[1,1,2]]))
print(unstable_gram([[2,-1,1],[1,0,3],[1,4,2]]))

print(stable_gram([[1,-1,1],[1,0,1],[1,1,2]]))
print(stable_gram([[2,-1,1],[1,0,3],[1,4,2]]))















