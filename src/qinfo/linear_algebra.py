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

def norm(v: np.ndarray) -> float:
    """
    Compute the norm of a vector.

    Parameters:
    v (list or numpy array): Input vector.

    Returns:
    float: The norm of the vector.
    """
    return np.sqrt(inner_product(v, v))

def normalize(v: np.ndarray) -> np.ndarray:
    """
    Normalize a vector.

    Parameters:
    v (list or numpy array): Input vector.

    Returns:
    numpy array: The normalized vector.
    """
    n = norm(v)
    if n == 0:
        raise ValueError("Cannot normalize the zero vector.")
    
    return v / n