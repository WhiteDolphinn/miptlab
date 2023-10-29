import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from mylib import *


x,y = get_data('f_u_24.csv')
x1, y1 = get_interp(x, y, 50)

a,b = get_data('f_u_33.csv')
a1, b1 = get_interp(a, b, 50)


x1_param = 0.9816
x2_param = 1.0205
plt.plot([0.96, 1.04], [0.707, 0.707])
plt.plot([x1_param, x1_param], [0.65, 0.75], linewidth=1, color='#FFD0D0')
plt.plot([x2_param, x2_param], [0.65, 0.75], linewidth=1, color='#ffd0d0')

plt.plot(x1, y1, color='orange')
plt.scatter(x, y, color='red')

a1_param = 0.9745
a2_param = 1.0257
plt.plot([a1_param, a1_param], [0.65, 0.75], linewidth=1, color='#d0ffd0')
plt.plot([a2_param, a2_param], [0.65, 0.75], linewidth=1, color='#d0ffd0')


plt.plot(a1, b1, color='#12FF12')
plt.scatter(a, b, color='green')

plt.xlabel("$f/f_0$")
plt.ylabel("$U/U_0$")

plt.text(0.982, 0.65, f"f/f0 = {x1_param}", color='red', fontsize=8)
plt.text(1, 0.71, f"f/f0 = {x2_param}", color='red', fontsize=8)


plt.text(0.955, 0.71, f"f/f0 = {a1_param}", color='green', fontsize=8)
plt.text(1.028, 0.71, f"f/f0 = {a2_param}", color='green', fontsize=8)

plt.savefig('f_f0_U_U0.png')
