"""
For this homework assignment we will take our work from HW01 and use it to
prepare a python script which will implement our algoirthms as python functions. 

For Problems #0-5 from HW01, Do the following.



1) Write your answer from HW01 in a comment.

2) Below the comment write a function which implements the algorithm from your
comment. If you find that you need to change your algorithm for your python
code, you must edit your answer in the comment. 

3) Test each of your functions on at least 2 inputs. 

4) Upload your .py file to a github repo named "Math_3430_Fall_2021"

This assignment is due by 11:59pm 09/27/2021. Do NOT upload an updated version to github
after that date. 
"""


#Example:

#Problem 00

"""
-The Three Questions

Q1: What do we have?

A1: Two vectors stored as lists. Denoted by the names vector_a and vector_b. 

Q2: What do we want?

A2: Their sum stored as a list.

Q3: How will we get there?

A3: We will create an empty list of the appropriate size and store the sums of
the corresponding components of vector_a and vector_b. 

-PsuedoCode

def add_vectors(vector_a,vector_b):

Initialize a result vector of 0's which is the same size as vector_a. Call this
vector result.

# Set each element of result to be equal to the desired sum.
for index in range(length(result)):
  result[index] = vector_a[index] + vector_b[index]

Return the desired result.
"""

def add_vectors(vector_a,vector_b):
  result = [0 for element in vector_a]
  for index in range(len(result)):
    result[index] = vector_a[index] + vector_b[index]
  return result

#End Example



#Problem 01
"""
Q1: What do we have?
We have a vector and a positive integer.
Q2: What do we want?
We want to multiply the vector by the positive integer.
Q3: How do we get there?
We have a positive integer n and we multiply it to every item in the vector list. Then we return the result.

Pseudocode:
def scalar_vector_mult(n, vector_01):
#Initialize result as empty list
    result = []
#Create a loop to multiply the vector by scalar.
    for i in range(len(vector_01)):
        vector_01[i] *= n
#Append new vector_01 to result
    result.append(vector_01)
#Return the desired result
    return result	
"""
def scalar_vector_mult(n, vector_01):
    result = []
    for i in range(len(vector_01)):
        vector_01[i] *= n
    result.append(vector_01)
    return result


print(scalar_vector_mult(8, [10,20,25]))
print("The answer should be [80,160,200]")
print(scalar_vector_mult(4, [10,20,25]))
print("The answer should be [40,80,100]")

#Problem 02
"""
Q1: What do we have?
We have a positive integer and a matrix.
Q2: What do we want?
We want to multiply the matrix by the positive integer and store the result as a list.
Q3: How do we get there?
We split the matrix into vectors and then using the method from problem 1 we get the multiple of the vectors and then put them back into a matrix form

Pseudocode:
def scalar_matrix_mult(n, matrix_a):
#Make the result list
    result = [scalar_vector_mult(n,matrix_a[0])]
#Make a for loop for the scalar multiplication.
    for j in range(len(matrix_a)):
            y = scalar_vector_mult
#Attach the new vectors  to the empty set.
            result.append(y)
#Return the desired result.
    return result
"""
def scalar_matrix_mult(n, matrix_a):
    result = [scalar_vector_mult(n,matrix_a[0])]
    for x in range(1, len(matrix_a)):
        y = scalar_vector_mult(n, matrix_a[x])
        result.append(y)
    return result

print(scalar_matrix_mult(10, [[2,2],[4,4]]))
print("The answer should be [[20,20],[40,40]]")
print(scalar_matrix_mult(5, [[3,3],[5,5]])) 
print("The answer should be [[15,15],[25,25]]")

#Problem 03
"""
Q1: What do we have?
We have two matrices.
Q2: What do we want?
We want the sum of the two matrices stored as a list.
Q3: How do we get there?
We set the matrices equal to the vectors that make them up and add the vectors together for the sum. 

Pseudocode:
def matrix_addition(vector_a, vector_b, vector_c, vector_d, vector_e, vector_f):

#Make list with the starting elements of the list given through the funciton add_vectors
    result = []
#Complete the addition between the two 3x3 matrices.
    for x in range(1, len(matrix_A)):
        y = add_vectors(matrix_A[x], matrix_B[x])
#Attach the sum of the matrices to the result set.
        result.append(y)
#Return the desired result.
    return result
"""
def matrix_addition(matrix_A, matrix_B):
    result = [add_vectors(matrix_A[0],matrix_B[0])]
    for x in range(1, len(matrix_A)):
        y = add_vectors(matrix_A[x], matrix_B[x])
        result.append(y)
    return result


print(matrix_addition([[2,5], [1,2], [5,1]], [[1,0], [0,1], [3,6]]))
print("The answer should be [[3, 5], [1, 3], [8, 7]]")
print(matrix_addition([[10,5], [12,6], [4,5]], [[1,0], [0,1], [3,6]]))
print("The answer should be [[11, 5], [12, 7], [7, 11]]")

#Problem 04
"""
Q1: What do we have?
We have a matrix and a vector.
Q2: What do we want?
We want to get the multiple of the two using a linear combination of columns method.
Q3: How do we get there?
Using the algorithms from problems 0 and 1. We set the vector values as scalars to the vectors in the matrix. Then we will multiply the scalars into the vectors to get new vectors. Then we will add the vectors together. Then we will return the result in a list.

Pseudocode:
def matrix_vector_mult(vector_a, matrix_A):
    result = []
#Referencing problem 0 and 1 we make the for loop apply the correct values to the new vectors.
    for x in range(len(matrix_A)):
        y = scalar_vector_mult(vector_a[x],matrix_A[x])
#Apply the new vectors to the result.
        result.append(y)
#Return desired result.
    return result
"""
def matrix_vector_mult(vector_a, matrix_A):
    result = []
    for x in range(len(matrix_A)):
        y = scalar_vector_mult(vector_a[x],matrix_A[x])
        
        result.append(y)
    return result
    

print(matrix_vector_mult([2,1],[[3,2],[4,5]]))
print("The answer should be ")
print(matrix_vector_mult([5,2],[[1,1],[3,5]]))
print("The answer should be ")

#Problem 05
"""
Q1: What do we have?
We have two matrices.
Q2: What do we want?
We want to get the multiple of the two using a prior algorithm.
Q3: How do we get there?
Using the algorithm from problem #4. We will split one of the matrices into vectors and then multiply those individual vectors into the remaining matrix. Then we will return the result.

Pseudocode:
def matrix_mult(vector_01, vector_02, vector_03, vector_a, vector_b, vector_c):
#Set matrix_b as the vectors a, b, and c.
    matrix_b = [vector_a, vector_b, vector_c]
    result = []
#Multiply the vectors of each matrix into each other.
    for i in range(len(matrix_b)):
       vector_a[i] = vector_a[i]*x + vector_a[i]*y + vector_a[i]*z + vector_a[i]*j + vector_a[i]*k + vector_a[i]*l + vector_a[i]*p + vector_a[i]*o + vector_a[i]*u
       vector_b[i] = vector_b[i]*x + vector_b[i]*y + vector_b[i]*z + vector_b[i]*j + vector_b[i]*k + vector_b[i]*l + vector_b[i]*p + vector_b[i]*o + vector_b[i]*u
       vector_c[i] = vector_c[i]*x + vector_c[i]*y + vector_c[i]*z + vector_c[i]*j + vector_c[i]*k + vector_c[i]*l + vector_c[i]*p + vector_c[i]*o + vector_c[i]*u
#Apply the answers to the result.
    result.append(vector_a)
    result.append(vector_b)
    result.append(vector_c)
#Return the desired result.
    return result
"""
def matrix_mult(vector_01, vector_02, vector_03, vector_a, vector_b, vector_c):
    matrix_b = [vector_a, vector_b, vector_c]
    result = []
    for i in range(len(matrix_b)):
       vector_a[i] *= vector_01[i]
       vector_b[i] *= vector_02[i]
       vector_c[i] *= vector_03[i]
    result.append(vector_a)
    result.append(vector_b)
    result.append(vector_c)
    return result

print(matrix_mult([3,4,5], [1,2,7], [9,6,8], [1,2,3], [2,1,3], [3,2,1]))
print("The answer should be [[3, 8, 15], [2, 2, 21], [27, 12, 8]]")
print(matrix_mult([4,5,6], [7,8,9], [1,2,3], [2,1,3], [10,5,1], [3,2,1]))
print("The answer should be [[8, 5, 18], [70, 40, 9], [3, 4, 3]]")

#Test Inputs

test_vector_01 = [1, 2, 4]
test_vector_02 = [3, 1, 2]

# add_vectors(test_vector_01,test_vector_02) should output [4,3,6]
print('Test Output for add_vectors: ' + str(add_vectors(test_vector_01,test_vector_02)))
print('Should have been [4,3,6]')
