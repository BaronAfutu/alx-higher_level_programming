#!/usr/bin/python3
"""Define a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Returns the multiplication of two matrices.

    Args:
        m_a (matrix of ints/floats): First matrix.
        m_b (matrix of ints/floats): Second matrix.
    """

    return (np.matmul(m_a, m_b))
