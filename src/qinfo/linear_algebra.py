import numpy as np

def inner_product(v: np.ndarray, w: np.ndarray): -> complex
    """
    Compute the inner product of two vectors a and b.

    Parameters:
    a (list or numpy array): First vector.
    b (list or numpy array): Second vector.

    Returns:
    complex: The inner product of a and b.
    """
    if len(v) != len(w):
        raise ValueError("Vectors must be of the same length.")
    
    return sum(x * y for x, y in zip(v, w))