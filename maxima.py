import numpy as np

def find_maxima(x):
    """Find local maxima of x.

    Example:
    >>> x = [1, 2, 3, 2, 4, 3]
    >>> find_maxima(x)
    [2, 4]

    Input arguments:
        x -- 1D list numbers

    Output:
        idx -- list of indices of the local maxima in x
    """

    idx = []
    bfr = []
    up = True
    for i in range(len(x)):
        # `i` is a local maximum if the signal decreases before and after it

        # starting or going up
        if i == 0 or x[i] > x[i-1]:
            up = True
            bfr = [i]
        # plateau
        elif x[i] == x[i-1]:
            if up:
                bfr.append(i)
        # going down
        elif x[i] < x[i-1]:
            up = False
            idx += bfr
            bfr = []
        # end
        if i == len(x) - 1:
            if up:
                idx += bfr                     
    return idx
