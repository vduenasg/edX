def ndigits(x):
    '''
    Counts how many digits has the number 'x'
    input  --> int (positive or negative)
    output --> int
    '''
    if abs(x/10) == 0:
        return 1
    # We will stop the recursion bucle when reach units
    else:
        return 1 + ndigits(abs(x/10))