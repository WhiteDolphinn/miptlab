import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from mylib import *


x,y = get_data('R_l.csv')
# x1, y1 = get_interp(x, y, 50)




#plt.plot(x1, y1, color='orange')
plt.scatter(x, y, color='red')

plt.plot([5, 32], [3.882, 3.882], color='blue')

plt.xlabel("$f, кГц$")
plt.ylabel("$R_l, Oм$")


plt.savefig('R_l.png')
