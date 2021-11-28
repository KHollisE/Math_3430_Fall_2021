import LA
import QR



def back_sub(matrix_1: list, vector_1: list)->list:
    """
    Gives the back substitution of an input matrix and input vector
    
    Create value m that takes the place of the length of the matrix minus one.
    Create a result vector from the input vector multiplied into one over the 
    value in the last row and column of input matrix. Create a loop and then
    an inner loop to solve for a temporary value then append that value to the
    result. Return result.
    
    Args:
        matrix_1: A matrix stored as a list of lists
        vector_1: A vector stored as a list.
    Returns:
        The back substitution.
    """
    m = len(matrix_1) + (-1)
    result: list = [vector_1[-1]*(1/(matrix_1[-1][-1]))]
    for x in range(m - 1, -1, -1):
        temp: float = vector_1[x]
        for y in range(len(result)):
            temp -= matrix_1[m - y][x] * result[y]
        temp *= 1/(matrix_1[x][x])
        result.append(temp)
    result = result[::-1]
    return result


def least_squares(matrix_a: list, vector_a: list)->list:
    """
    Give the least square matrix.
    
    Use stable gram schmitt to get a Q and R of the input
    matrix. Take the conjugate transpose of Q. Do matrix vector multiplication
    with the input vector and the Q transpose. Then use back substitution to
    get the result. Return the result.
    
    Args:
        matrix_a: A matrix stored as a list of lists
        vector_a: A vector stored as a list.
    Returns:
        The least square matrix.
    """
    Q,R = QR.stable_gram(matrix_a)
    Q_trans = QR.conjugate_transpose(Q)
    Q_b = LA.matrix_vector_mult(vector_a, Q_trans)
    result = back_sub(R, Q_b)
    return result












