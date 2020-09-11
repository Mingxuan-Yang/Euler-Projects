# Euler Project Problem 31

def coin_sum(coins, target):
    """Return the number of combinations of currency denominations.
    
    This function can be used to solve problems like how many different ways can the value
    `target` be made using any number of values within `coins`.
    
    Parameters
    ----------
    coins : array_like
        All possible values that can be used to make up the `target` value. These values 
        should be integers. In the context of currency denomination, all of the values 
        within `coins` should have the same units, which is also the minimum unit. For 
        example, if `coins` contains both penny and pound, the values should be represented
        by pence unit, which accords with the integral requirement.
        
    target : int
        The resulting total value. In the context of currency denomination, it needs to 
        have the same unit with values in `coins`.
        
    Returns
    -------
    int
        The number of possible combinations to make up `target` using values in `coins`.
        
    Examples
    --------
    The number of different ways to make up 2 pounds using 8 possible coins: 1 penny, 
    2 pence, 5 pence, 10 pence, 20 pence, 50 pence, 1 pound, and 2 pounds.

    >>> coin_sum([1, 2, 5, 10, 20, 50, 100, 200], 200)
    73682
    """
    numbers = [1]*(target + 1)
    
    for i in coins[1:]:
        for j in range(i, target+1):
            numbers[j] += numbers[j-i]
            
    return int(numbers[target])

print(coin_sum([1, 2, 5, 10, 20, 50, 100, 200], 200))