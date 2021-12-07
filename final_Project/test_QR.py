import QR
import pytest


pytest.main()

matrix_01 = [[1,-1,1],[1,0,1],[1,1,2]]
matrix_02 = [[2,-1,1],[1,0,3],[1,4,2]]
matrix_03 = [[2,2,1],[-2,1,2],[18,0,0]]
matrix_04 = [[1,5],[3,7]]

#Test Q_orthonormal function
def test_Q_orthonormal_1():
    assert QR.Q_orthonormal(matrix_01) == ([[0.5773502691896258, -0.5773502691896258, 0.5773502691896258], [0.40824829046386274, 0.8164965809277261, 0.40824829046386274], [-0.7071067811865468, 6.280369834735101e-16, 0.7071067811865482]])
def test_Q_orthonormal_2():
    assert QR.Q_orthonormal(matrix_02) == ([[0.8164965809277261, -0.4082482904638631, 0.4082482904638631], [-0.2760262237369418, 0.3450327796711771, 0.8970852271450603], [0.50709255283711, 0.8451542547285165, -0.16903085094570308]])

#Tests stable_gram function
def test_stable_gram_1():
    assert QR.stable_gram(matrix_01) == ([[0.5773502691896258, -0.5773502691896258, 0.5773502691896258], [0.40824829046386274, 0.8164965809277261, 0.40824829046386274], [-0.7071067811865468, 6.280369834735101e-16, 0.7071067811865482]], [[1.7320508075688776, 0, 0], [1.1547005383792517, 0.816496580927726, 0], [1.1547005383792517, 2.0412414523193148, 0.7071067811865475]])
def test_stable_gram_2():
    assert QR.stable_gram(matrix_02) == ([[0.8164965809277261, -0.4082482904638631, 0.4082482904638631], [-0.2760262237369418, 0.3450327796711771, 0.8970852271450603], [0.50709255283711, 0.8451542547285165, -0.16903085094570308]], [[2.4494897427831783, 0, 0], [2.041241452319315, 2.4152294576982394, 0], [0.0, 2.8982753492378874, 3.5496478698597693]])

#Tests sign function
def test_sign_1():
    assert QR.sign(4) == 1
def test_sign_2():
    assert QR.sign(-2) == -1

#Tests reflect_vector function
def test_reflect_vector_1():
    assert QR.reflect_vector(matrix_01[1]) == [2.414213562373095, 0.0, 1.0]
def test_reflect_vector_2():
    assert QR.reflect_vector(matrix_03[0]) == [5.0, 2.0, 1.0]
    
#Tests Identity function
def test_Identity_1():
    assert QR.Identity(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
def test_Identity_2():
    assert QR.Identity(2) == [[1, 0], [0, 1]]
    
#Tests vector vector multiplication function
def test_vec_vec_mult_1():
    assert QR.vec_vec_mult([5,2,1], [5,2,1]) == [[25, 10, 5], [10, 4, 2], [5, 2, 1]]
def test_vec_vec_mult_2():
    assert QR.vec_vec_mult([2.414213562373095, 0.0, 1.0], [2.414213562373095, 0.0, 1.0]) == [[5.82842712474619, 0.0, 2.414213562373095], [0.0, 0.0, 0.0], [2.414213562373095, 0.0, 1.0]]
    
#Tests F_builder function
def test_F_builder_1():
    assert QR.F_builder([4.8, 2.4]) == [[-0.6000000000000001, -0.8], [-0.8, 0.6]]
def test_F_builder_2():
    assert QR.F_builder([2.4, 4.8]) == [[0.6, -0.8], [-0.8, -0.6000000000000001]]

#Tests Q_build function
def test_Q_build_1():
    assert QR.Q_build(matrix_01, 1) == [[1, 0, 0], [0, 2.220446049250313e-16, -0.9999999999999998], [0, -0.9999999999999998, 2.220446049250313e-16]]
def test_Q_build_2():
    assert QR.Q_build(matrix_02, 1) == [[1, 0, 0], [0, -2.220446049250313e-16, -1.0000000000000002], [0, -1.0000000000000002, -2.220446049250313e-16]]

#Tests deep copy function
def test_deep_copy_1():
    assert QR.deep_copy(matrix_01) == [[1,-1,1],[1,0,1],[1,1,2]]
def test_deep_copy_2():
    assert QR.deep_copy(matrix_02) == [[2,-1,1],[1,0,3],[1,4,2]]

#Tests conjugate transpose function
def test_conjugate_transpose_1():
    assert QR.conjugate_transpose([[1,3],[2,5]]) == [[1, 2], [3, 5]]
def test_conjugate_transpose_2():
    assert QR.conjugate_transpose(matrix_01) == [[1, 1, 1], [-1, 0, 1], [1, 1, 2]]
    
#Tests householder funciton
def test_householder_1():
    assert QR.householder(matrix_03) == ([[-0.6666666666666667, -0.6666666666666666, -0.3333333333333333], [0.6666666666666667, -0.3333333333333334, -0.6666666666666667], [-0.33333333333333337, 0.6666666666666667, -0.6666666666666666]], [[-3.0000000000000004, -1.1657341758564147e-16, 1.5543122344752193e-16], [2.220446049250313e-16, -3.0, 0.0], [-12.000000000000002, 12.000000000000002, -6.000000000000002]])
def test_householder_2():
    assert QR.householder(matrix_04) == ([[-0.19611613513818393, -0.9805806756909202], [0.9805806756909202, -0.19611613513818393]], [[-5.099019513592785, 5.551115123125783e-16], [-7.4524131352509935, 1.568929081105473]])