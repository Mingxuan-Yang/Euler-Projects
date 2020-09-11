# Euler Project Problem 85

def counting(target, max_width = None, max_length = None):
    """Return the area of the grid with the nearest number of possible rectangles compared 
    with `target`.
    
    The sides of the grid and the possible rectangles are integers that are equal or greater 
    than 1. If there exists a grid which contains exactly `target` number of rectangles, the 
    corresponding area will be the returning result. Otherwise, the area of the grid 
    containing the closest number will be returned.
    
    Parameters
    ----------
    target : int
        The desired number of possible rectangles. It should be positive. If no grid has 
        exactly `target` number of rectangles, the grid containing the closest number will 
        be applied.
        
    max_width : int, optional
        The maximum width of the resulting grid. It should be positive. If `max_width` is not 
        given, the value ⌈(4n)^{1/4}⌉, where n is the value of 
        `target`, will be employed based on the following formula.
        
            n = x(x + 1)y(y + 1)/4
        
        Here x and y represent the width and length of the grid. y is implicitly larger 
        than x. Therefore, the maximum value of x is equal to y. After calculation, it 
        should be approximately ⌈(4n)^{1/4}⌉.
        
    max_length : int, optional
        The maximum length of the resulting grid. It should be positive. If `max_length` is 
        not given, the value ⌈(2n)^{1/2}⌉, where n is the value of 
        `target`, will be employed based on the following formula.
        
            n = x(x + 1)y(y + 1)/4
        
        Here x and y represent the width and length of the grid. y is implicitly larger 
        than x. When x is equal to 1, y will reach its maximum value. After calculation, 
        it should be approximately ⌈(2n)^{1/2}⌉.
        
    Returns
    -------
    int
        The area of the grid which has the nearest number of possible rectangles compared 
        with `target`.
        
    Examples
    --------
    The area of the grid with almost two millions number of possible rectangles.

    >>> counting(2000000)
    2772
    """
    if not max_width:
        max_width = int((4*target)**(1/4) // 1 + 1)
    if not max_length:
        max_length = int((2*target)**(1/2) // 1 + 1)
    diff_min = target
    
    for i in range(1, max_width + 1):
        for j in range(i, max_length + 1):
            diff = abs(i*(i+1)*j*(j+1)/4 - target)
            if diff < diff_min:
                area, diff_min = i*j, diff
    
    return area

print(counting(2000000))