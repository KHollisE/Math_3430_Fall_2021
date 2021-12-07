import LA
import QR
import LS


print("Hi my name is Kevin Hollis.")
print("This is a library containing functions from six files.")
print("These are LA.py, QR.py, LS.py, and the test files of those three.")
print("")

print("LA.py contains a large number of functions for performing basic linear algebra tasks.")
print("")

print("The first function in LA.py is add_vectors. It will take in two vectors as its arguments and return their sum.")
print("")
print("For example, if a = [2,1] and b = [3,2], then add_vectors(a,b) will return")
a = [2,1]
b = [3,2]
print(LA.add_vectors(a,b))
print("")

print("The second function in LA.py is scalar_vector_mult. It will take in a scalar and a vector as its arguments and return the product of them.")
print("")
print("For example, if n = 4 and vector_01 = [2,1], then scalar_vector_mult will return")
n = 4
vector_01 = [2,1]
print(LA.scalar_vector_mult(n, vector_01))
print("")

print("The third function in LA.py is scalar_matrix_mult. It will take in a scalar and a matrix as its arguments and return the product them.")
print("")
print("For example, if n = 4 and matrix_a = [[3,2],[4,5]], then scalar_matrix_mult will return")
matrix_a = [[3,2],[4,5]]
print(LA.scalar_matrix_mult(n, matrix_a))
print("")

print("The fourth function in LA.py is matrix_addition. It will take in two matrices as its arguments and return their sum.")
print("")
print("For example, if matrix_A = [[3,2],[4,5]] and matrix_B = [[1,1],[3,5]], then matrix_addition will return")
matrix_A = [[3,2],[4,5]]
matrix_B = [[1,1],[3,5]]
print(LA.matrix_addition(matrix_A, matrix_B))
print("")

print("The fifth function in LA is matrix_vector_mult. It will take in a vector and a matrix as its arguments and return the product of them.")
print("")
print("For example, if vector_a = [2,1] and matrix_A = [[3,2],[4,5]], then matrix_vector_mult will return")
vector_a = [2,1]
print(LA.matrix_vector_mult(vector_a, matrix_A))
print("")

print("The sixth function in LA is matrix_mult. It will take two matrices as its arguments and return their product.")
print("")
print("For example, if matrix_A = [[3,2],[4,5]] and matrix_B = [[1,1],[3,5]], then matrix_mult will return")
print(LA.matrix_mult(matrix_A, matrix_B))
print("")

print("The seventh function in LA is p_norm. It will take a vector as a list and a scalar as a float and return the p-norm of the vector.")
print("")
print("For example, if vector = [2,1] and scalar = 2, then p_norm will return")
vector = [2,1]
scalar = 2
print(LA.p_norm(vector, scalar))
print("")

print("The eighth function in LA is infinity_norm. It will take a vector and return its infinity norm.")
print("")
print("For example, if vector = [3,2], then infinity_norm will return")
vector = [3,2]
print(LA.infinity_norm(vector))
print("")

print("The ninth function in LA is boolean_norm. It will take a vector, a float which defaults to 2, and a boolean value which defaults to False as its arguments and return either the p-nrom or the infinity norm.")
print("")
print("For example, if vector = [2,1], then boolean_norm will return")
vector = [2,1]
print(LA.boolean_norm(vector))
print("")

print("The tenth function in LA is inner_product. It will take in two vectors as its arguments and return their inner product.")
print("")
print("For example, if vector_a = [2,1] and vector_b = [3,2], then inner_product will return")
vector_a = [2,1]
vector_b = [3,2]
print(LA.inner_product(vector_a, vector_b))
print("")

print("QR contains a few functions for performing factorization.")
print("")

print("The first function in QR is stable_gram. It will take a matrix as its argument and return the reduced QR factorization.")
print("")
print("For example, if matrix_A = [[1,-1,1],[1,0,1],[1,1,2]], then stable_gram will return")
matrix_A = [[1,-1,1],[1,0,1],[1,1,2]]
print(QR.stable_gram(matrix_A))
print("")

print("The second function in QR is Q_orthonormal. It will take a matrix as its argument and return the reduced Q factorization.")
print("")
print("For example, if matrix_A = [[1,-1,1],[1,0,1],[1,1,2]], then Q_orthonormal will return")
print(QR.Q_orthonormal(matrix_A))
print("")

print("The third function in QR is householder. It will take a matrix as its argument and return the reduced QR factorization.")
print("")
print("For example, if matrix_A = [[2,2,1],[-2,1,2],[18,0,0]], then householder will return")
matrix_A = [[2,2,1],[-2,1,2],[18,0,0]]
print(QR.householder(matrix_A))
print("")

print("LS contains funcitons to perform least squares.")
print("")

print("The function in LS is least_squares. It will take a matrix and a vector as its arguments and return the least square matrix.")
print("")
print("For example, if matrix_a = [[2,3,1],[4,4,2],[1,1,1]] and vector_a = [1,2,1], then least_squares will return")
matrix_a = [[2,3,1],[4,4,2],[1,1,1]]
vector_a = [1,2,1]
print(LS.least_squares(matrix_a, vector_a))
print("")


