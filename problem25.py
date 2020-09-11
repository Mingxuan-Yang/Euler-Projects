# Euler Project Problem 25

def Fibonacci_digit(n):
    """Return the index of the first term in the Fibonacci sequence to contain n digits.
    
    The Fibonacci sequence is defined by the recurrence relation:
        F(n) = F(n-1) + F(n-2), where F(1) = F(2) = 1.
    
    Parameters
    ----------
    n : int
        The resulting number of digits. The Fibonacci sequence at the resulting index is
        desired to contain `n` digits.
        
    Returns
    -------
    int
        The index of the first term in the Fibonacci sequence that contains `n` digits.
        
    Examples
    --------
    The index of the first term in the Fibonacci sequence containing 3 digits.

    >>> Fibonacci_digit(3)
    12
    
    The index of the first term in the Fibonacci sequence containing 1000 digits.
    
    >>> Fibonacci_digit(1000)
    4782
    """
    if n == 1:
        return 1
    
    F = [1,1]
    while len(str(F[-1])) < n:
        F.append(F[-1] + F[-2])
        
    return F.index(F[-1]) + 1

print(Fibonacci_digit(1000))