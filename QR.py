import LA


#Problem 2 for HW06
def Q_orthonormal(matrix_A: list)->list:
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
    



def sign(x: int)->int:
    """
    Determines the sign
    
    Checks if value x is less then or greater than zero. Then returns either
    -1 or 1.
    
    Args:
        x: A number stored as a int
    Returns:
        Either -1 or 1
    """
    if x >= 0:
        return 1
    else:
        return -1
    
def reflect_vector(vector_1: list)->list:
    """
    Gives the reflection of an input vector
    
    Creates a vector e with the first index of that vector being 1. Then using
    prior functions add_vectors, scalar_vector_mult, and boolean_norm
    from LA and references prior funciton signs solves for v.
    
    Args:
        vector_1: A vector stored as a list
    Returns:
        Reflection of input vector
    """
    e = [0 for element in range(len(vector_1))]
    e[0] = 1
    v = LA.add_vectors(LA.scalar_vector_mult(sign(vector_1[0])*LA.boolean_norm(vector_1),e),vector_1)
    return v

def Identity(size: int)->int:
    """
    Creates an identity matrix
    
    Makes a matrix of input size with zeroes. Then replaces the diagnol
    elements in the matrix with 1.
    
    Args:
        size: A number stored as an integer
    Returns:
        The identity matrix
    """
    ident: list = [[0 for element in range(size)]for index in range(size)]
    for x in range(size):
        for y in range(size):
            ident[x][x] = 1         
    return ident

def vec_vec_mult(vector_1: list, vector_2: list)->list:
    """
    Give the product of two vectors
    
    Creates and empty list. Appends the LA.scalar_vector_mult of vector_1
    and vector_2 to the empty set. Returns the result.
    
    Args:
        vector_1: A vector stored as a list
        vector_2: A vecctor stored as a list 
    Returns:
        The vector-vector multiplication of two input vectors
    """
    result: list = []
    for x in range(len(vector_1)):
        result.append(LA.scalar_vector_mult(vector_1[x], vector_2))
    return result
        
def F_builder(vector_1: list)->list:
    """
    Creates the F_k value of the Q_build function
    
    Sets element s as -2/(LA.boolean_norm(vector_1))**2. Then sets element x
    as the scalar matrix mult of s and the vector-vector multiplication of 
    vector_1. Then does matrix addition with x and the identity matrix.
    Returns the result.
    
    Args:
        vector_1: A vector stored as a list.
    Returns:
        The F_k value.
    """
    s = -2/(LA.boolean_norm(vector_1))**2
    x = LA.scalar_matrix_mult(s, vec_vec_mult(vector_1, vector_1))
    y = LA.matrix_addition(Identity(len(vector_1)), x)
    return y

def Q_build(mtx: list, n: int)->list:
    """
    Creates a part of the householder function
    
   Create a matrix A of zeroes. Set a for loop with inner for loop that checks
   for if the range is overshot. Then get the refleciton vector for the recently
   replaced list. Then take the F_builder of that value. Set Q to the identity
   matrix. Go to a smaller section of the matrix and impliment the F_builder 
   into the Identity matrix. Then return Q.
   
   Args:
       mtx: A matrix stored as a list
   Returns:
       The Q value to solve for R in householder.
    """
  
    A:list = [[0 for j in range (n, len(mtx[i]))]for i in range(n,len(mtx))]    
    for i in range(len(mtx)):         
        for j in range(len(mtx[i])):             
            if n+i < len(mtx[i]):                 
                if n+j < len(mtx[i]):                     
                    A[i][j] = mtx[n+i][n+j]         
    v = reflect_vector(A[0])         
    f = F_builder(v)     
    Q = Identity(len(mtx))     
    for i in range(n,len(Q)):         
        for j in range(n,len(Q)):             
            Q[i][j] = f[i-n][j-n]     
    return Q


def deep_copy(matrix_1: list)->list:
    """
    Creates a copy of a matrix
    
    Makes a matrix of zeroes. Replaces the zeroes in the matrix with the 
    corresponding values of another matrix. Returns a matrix.
    
    Args:
        matrix_1: A matrix stored as a list of lists.
    Returns:
        A copy of the input matrix.
    """
    empty: list = [[0 for element in range(len(matrix_1[0]))]for index in range(len(matrix_1))]
    for x in range(len(matrix_1[0])):
        for y in range(len(matrix_1[0])):
            empty[x][y] = matrix_1[x][y]
    return empty


def conjugate_transpose(matrix_1: list)->list:
    """
    Gives the conjugate transpose of an input matrix.
    
    Creates two matrices of similar dimensions to the input matrix filled with 
    zeroes. Replaces one of the matrices' elements with the corresponding
    elements of the conjugated input matrix. Then changes the rows and columns
    with the use of the remaining matrix of zeroes. Returns the result.
    
    Args:
        matrix_1: A matrix stored as a list of lists.
    Returns:
        The conjugate transpose of an input matrix.
    """
    empty: list = [[0 for element in range(len(matrix_1[0]))]for index in range(len(matrix_1))]
    empty_2: list = [[0 for element in range(len(matrix_1[0]))]for index in range(len(matrix_1))]
    for x in range(len(matrix_1[0])):
        for y in range(len(matrix_1[0])):
            empty[x][y] = (matrix_1[x][y].conjugate())
    for i in range(len(matrix_1[0])):
        for j in range(len(matrix_1)):
            empty_2[i][j] = empty[j][i]
            
    return empty_2

def householder(matrix_A: list)->list:
    """
    Gives the householder QR factorization
    
    Takes R as a copy of the input matrix. Create an empty set. Call Q_build
    to create values to solve for R with matrix multiplication. Append the 
    values created in Q_build to empty list. Set Q equal to the last index in 
    new filled list. Take the cojugate transpose of the first vector of the 
    new list. Take the matrix multiple of Q and the conjugate transpose of the
    indices of the new list. Return the QR factorization.
    
    Args:
        matrix_A: A matrix stored as a list.
    Returns:
        The QR factorization.
    """
    R: list = deep_copy(matrix_A)
    Q_list: list = []
    for k in range(len(R)):
        Q_temp: list= Q_build(R, k)
        
        R = LA.matrix_mult(Q_temp, R)
        
        Q_list.append(Q_temp)
    Q: list = Q_list[-1]
    Q: list = conjugate_transpose(Q_list[0])
    for index in range(1, len(Q_list)):
          Q = LA.matrix_mult(Q, conjugate_transpose(Q_list[index]))
    return Q, R

#A[0][0:] brings out a subvector of a matrix.
"""
print(householder([[2,2,1],[-2,1,2],[18,0,0]]))
print(householder([[1,5],[3,7]]))
    
print(F_builder([4.8, 2.4]))
  
print(vec_vec_mult([5,2,1],[5,2,1]))

print(reflect_vector([2,2,1]))

print(conjugate_transpose([[1,3],[2,5]]))

print(Q_orthonormal([[1,-1,1],[1,0,1],[1,1,2]]))
print(Q_orthonormal([[2,-1,1],[1,0,3],[1,4,2]]))

print(stable_gram([[1,-1,1],[1,0,1],[1,1,2]]))
print(stable_gram([[2,-1,1],[1,0,3],[1,4,2]]))
"""