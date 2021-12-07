

def add_vectors(vector_a: list,vector_b: list)->list:
    """
    Adds the two input vectors.

    Creates a result vector stored as a list of 0's the same length as the input 
    then overwrites each element of the result vector with the corresponding
    element of the sum of the input vectors. Achieves this using a for loop over
    the indices of result. 

    Args:
        vector_a: A vector stored as a list.
        vector_b: A vector, the same length as vector_a, stored as a list.

    Returns:
       The sum of the input vectors stored as a list. 
    """
    
    result: list = [0 for element in vector_a]
    for index in range(len(result)):
        result[index] = vector_a[index] + vector_b[index]
    return result



def scalar_vector_mult(n: float, vector_01: list)->list:
    """
    Multiplies a scalar input into a vector input.
    
    Creates an empty set. Then appends the products of input n and 
    indices in the input vector. Achieves this using a for loop.
    
    Args:
        n: Scalar value stored as a float.
        vector_01: Vector stored as a list.
    
    Returns:
        The product result of the input n into input vector.
    """
    result: list = []
    #Following format of 0 for element we create a for loop to multiply scalars 
    #into the vectors.
    for i in vector_01:
        result.append(n * i)
    return result



def scalar_matrix_mult(n: float , matrix_a: list)->list:
    """
    Multiplies a scalar input into a matrix input.
    
    Creates a list resulting from the product first indices of the matrix
    with n. Then with a for loop it computes the proceeding products and appends 
    them to the list.
    
    Args:
        n: Scalar value stored as a float.
        matrix_a: Matrix stored as a list.
    
    Returns:
        The product result of the input n into input matrix.
    """
    result: list = [scalar_vector_mult(n,matrix_a[0])]
    for x in range(1, len(matrix_a)):
        y = scalar_vector_mult(n, matrix_a[x])
        result.append(y)
    return result



def matrix_addition(matrix_A: list, matrix_B: list)->list:
    """
    Adds two input matrices.
    
    Creates an empty set. Then with a for loop it adds the corresponding
    vectors in the matrices to each other. Then appends them to the list. Result
    is the sum of the vectors.
    
    Args:
        matrix_A: Matrix stored as a list.
        matrix_B: Matrix, the same perameter as matrix_A, stored as a list.
        
    Returns:
        The sum of the matrices.
    """
    result: list = []
    for x in range(len(matrix_A)):
        y = add_vectors(matrix_A[x], matrix_B[x])
        result.append(y)
    return result



def matrix_vector_mult(vector_a: list, matrix_A: list)->list:
    """
    Multiplies an vector input into a matrix input.
    
    Creates a list of 0's the same length as the matrix input. Then with a for
    loop it overwrites the indices in the list of 0's with the corresponding 
    indices from the product of the vector input and the matrix input. Then it adds the 
    vectors from the result into each while checking to verify if the length
    of the result is more than two to determine if more vectors need to be added into 
    the result y. If not it just returns the result.
    
    Args:
        vector_a: Vector stored as a list.
        matrix_A: Matrix, with the same length as vector_a, stored as a list.
    
    Returns:
        The product of a matrix and a vector.
        
    """
    result: list = [0 for element in matrix_A]
    for index in range(len(matrix_A)):
        result[index] = scalar_vector_mult(vector_a[index],matrix_A[index])

    y: list = add_vectors(result[0],result[1])

    if (len(result)>2):
        i = 0
        while i < (len(result)-2):
            y = add_vectors(y,result[i+2])
            i += 1
        return y
    else:
        return y



def matrix_mult(matrix_A: list, matrix_B: list):
    """
    Multiplies two matrices.
    
    Creates an empty list. Using a for loop it take the algorithm from previous
    problem and takes the result of it with corresponding values and appends it to the
    empty set. 
    
    Args:
        matrix_A: Matrix stored as a list.
        matrix_B: Matrix, with the same length as previous, stored as a list.
    
    Returns:
        The product of the matrices.
    """
    result: list = []
    for x in range(len(matrix_A[0])):
        result.append(matrix_vector_mult(matrix_B[x],matrix_A))
    return result




def absolute_value(scalar: complex)->float:
    """
    Takes the absolute value of complex and real numbers
    
    Takes the scalar input and gets the conjugate. Then it multiplies the
    conjugate into the orginal input, and then take the square root of the
    product. Then returns the value.
    
    Args:
        scalar: A complex or real number.
    Returns:
        The absolute value of the input.
    """
    z = scalar.conjugate()
    x: float = (z*scalar)**(1/2)
    return x.real




def p_norm(vector: list, scalar: float)->float:
    """
    Gives the p-norm of a vector.
    
    Sets a result equal to zero. Then takes the absolute value of the indices 
    in the vector and then puts that value to the power of the scalar input. 
    Then it sums all the indices together. Returns result.
    
    Args:
        vector: A vector stored as a list.
        scalar: A scalar stored as a float.
    Returns:
        The p-norm of the vector.
    """
    result: float = 0
    for index in vector:
        y = (absolute_value(index))**scalar
        result = result + y
    return result**(1/scalar)




def infinity_norm(vector: list)->float:
    """
    Gives the infinity-norm of a vector.
    
    Sets a result equal to an empty list of float values. Then it takes the 
    absolute value of the indices in the vector input and appends that to the
    empty set result. Then it return the indices value that is the greatest.
    
    Args:
        vector: A vector stored as a list.
    Returns:
        The infinity norm of a vector.
    """
    result: list[float] = []
    for index in vector:
        y = absolute_value(index)
        result.append(y)
    return max(result)




def boolean_norm(vector: list, boolean: bool = False, scalar: float = 2)->float:
    """
    Gives the p-norm or infinity-norm of a vector.
    
    Determines if boolean input is true. If it is then the funciton returns the
    infinity-norm. If not it returns the p-norm.
    
    Args:
        vector: A vector stored as a list.
        boolean: A boolean defaultly stored as False.
        scalar: A scalar stored as a float.
    Returns:
        The infinity-norm or the p-norm.
    """
    if boolean == True:
        x: list[float] = infinity_norm(vector)
    else:
        x: float = p_norm(vector, scalar)
    return x




def inner_product(vector_a: list, vector_b: list)->float:
    """
    Gives the inner product of two vectors.
    
    Creates a result value equal to zero. Then with a for loop multiplies the
    two vectors respective index into each other. Then the sum of the products 
    is returned.
    
    Args:
        vector_a: A vector stored as a list.
        vector_b: A vector, of same length a vector_a, stored as a list.
    Returns:
        The inner product.
    """
    result: float = 0
    for index in range(len(vector_a)):
        y = vector_a[index]*vector_b[index]
        result = result + y
    return result


