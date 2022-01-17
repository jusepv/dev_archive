import numpy as np

def moving_average(x, w):
    '''
    x : numpy
    w : width
    '''
    return np.convolve(x, np.ones(w), 'valid') / w