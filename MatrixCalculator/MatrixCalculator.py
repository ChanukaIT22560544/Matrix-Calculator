import numpy as np

def matrix_addition(A, B):
    if A.shape != B.shape:
        raise ValueError("Matrices must have the same dimensions for addition.")
    return A + B

def matrix_subtraction(A, B):
    if A.shape != B.shape:
        raise ValueError("Matrices must have the same dimensions for subtraction.")
    return A - B

def matrix_multiplication(A, B):
    if A.shape[1] != B.shape[0]:
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
    return A @ B

def matrix_determinant(A):
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square to compute the determinant.")
    return np.linalg.det(A)

def matrix_inverse(A):
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square to compute the inverse.")
    return np.linalg.inv(A)
