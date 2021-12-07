import LS
import pytest

pytest.main()


matrix_1 = [[1,0,0],[3,2,0],[-1,2,4]]
matrix_2 = [[2,3,1],[4,4,2],[1,1,1]]
matrix_3 = [[1,1,1],[1,2,3],[1,4,9]]

vector_a = [1/2,-3/2,-3]
vector_b = [1,-2,-3]
vector_c = [1,2,1]
vector_d = [4,7,12]

#Tests back substitution.
def test_back_sub_1():
    assert LS.back_sub(matrix_1, vector_a) == [-0.25, 0.0, -0.75]
def test_back_sub_2():
    assert LS.back_sub(matrix_1, vector_b) == [1.0, -0.25, -0.75]

#Tests least squares.
def test_least_squares_1():
    assert LS.least_squares(matrix_2, vector_c) == [1.0000000000000004, -0.5000000000000008, 1.0000000000000018]
def test_least_squares_2():
    assert LS.least_squares(matrix_3, vector_d) == [3.000000000000011, -6.908406818208611e-15, 1.0000000000000004]



