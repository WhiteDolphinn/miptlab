import numpy as np
from scipy.interpolate import CubicSpline

def get_data(path):
    my_data = np.genfromtxt(path, delimiter=',')
    x = my_data[:,0]
    y = my_data[:,1]
    return x,y

def get_interp(x, y, count = 50):
    a = sorted(zip(x,y))
    x = [i[0] for i in a]
    y = [i[1] for i in a]
    spl = CubicSpline(x, y)

    x1 = np.linspace(min(x), max(x), count)
    y1 = [spl(i) for i in x1]
    return x1,y1
