
import LA
import pytest


pytest.main()

n = 4

test_vector_01 = [2,1]
test_vector_02 = [3,2]
test_vector_03 = [1,1]

test_matrix_01 = [[3,2],[4,5]]
test_matrix_02 = [[1,1],[3,5]]
test_matrix_03 = [[2,2],[5,6]]

#Tests for add_vectors function
def test_add_vectors_0():
    assert LA.add_vectors(test_vector_01, test_vector_02) == [5,3]
def test_add_vectors_1():
    assert LA.add_vectors(test_vector_02, test_vector_03) == [4,3]
    
#Tests for scalar_vector_mult function
def test_scalar_vector_mult_0():
    assert LA.scalar_vector_mult(n, test_vector_01) == [8,4]
def test_scalar_vector_mult_1():
    assert LA.scalar_vector_mult(n, test_vector_02) == [12,8]
    
#Tests for scalar_matrix_mult function
def test_scalar_matrix_mult_0():
    assert LA.scalar_matrix_mult(n, test_matrix_01) ==[[12,8],[16,20]]
def test_scalar_matrix_mult_1():
    assert LA.scalar_matrix_mult(n, test_matrix_02) ==[[4,4],[12,20]]
    
#Tests for matrix_addition function
def test_matrix_addition_0():
    assert LA.matrix_addition(test_matrix_01, test_matrix_02) == [[4,3],[7,10]]
def test_matrix_addition_1():
    assert LA.matrix_addition(test_matrix_02, test_matrix_03) == [[3,3],[8,11]]
    
#Tests for matrix_vector_mult function
def test_matrix_vector_mult_1():
    assert LA.matrix_vector_mult(test_vector_01,test_matrix_01) == [10,9]
def test_matrix_vector_mult_2():
    assert LA.matrix_vector_mult(test_vector_01,test_matrix_02) == [5,7]
    
#Tests for matrix_mult function
def test_matrix_mult_1():
    assert LA.matrix_mult(test_matrix_01,test_matrix_02) == [[7,7],[29,31]]
def test_matrix_mult_2():
    assert LA.matrix_mult(test_matrix_01,test_matrix_03) == [[14,14],[39,40]]
