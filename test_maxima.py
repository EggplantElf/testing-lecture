from maxima import find_maxima
import numpy as np

def test_1():
    assert find_maxima([0, 1, 2, 1, 2, 1, 0]) ==  [2, 4]

def test_2():
    assert find_maxima([2,1,0,1,4]) ==  [0, 4]

def test_3():
    assert find_maxima([np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]) ==  [16, 78]

def test_4():
    assert find_maxima([1, 2, 2, 3, 1]) ==  [3]


def test_5():
    assert find_maxima([1, 3, 2, 2, 1]) ==  [1]


def test_6():
    assert find_maxima([3, 2, 2, 3]) ==  [0, 3]

def test_6():
    assert find_maxima([1, 2, 2, 1]) ==  [1, 2]