import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from mylib import *


x,y = get_data('fchkh1.csv')

x1, y1 = get_interp(x, y, 50)



a,b = get_data('fchkh2.csv')
a1, b1 = get_interp(a, b, 50)

x1_param = 0.977
x2_param = 0.983
plt.plot([x1_param, x1_param], [0.7, 0.8], linewidth=1, color='#FFD0D0')
plt.plot([x2_param, x2_param], [0.7, 0.8], linewidth=1, color='#ffd0d0')

plt.plot(x1, y1, color='orange')
plt.scatter(x, y, color='red')

a1_param = 1.0225
a2_param = 1.0265
plt.plot([a1_param, a1_param], [0.2, 0.3], linewidth=1, color='#d0ffd0')
plt.plot([a2_param, a2_param], [0.2, 0.3], linewidth=1, color='#d0ffd0')


plt.plot(a1, b1, color='#12FF12')
plt.scatter(a, b, color='green')

plt.xlabel("$f/f_0$")
plt.ylabel("$\phi/\phi_0$")

# plt.text(0.982, 0.65, f"f/f0 = {x1_param}", color='red', fontsize=8)
# plt.text(1, 0.71, f"f/f0 = {x2_param}", color='red', fontsize=8)
#
#
# plt.text(0.955, 0.71, f"f/f0 = {a1_param}", color='green', fontsize=8)
# plt.text(1.028, 0.71, f"f/f0 = {a2_param}", color='green', fontsize=8)

plt.plot([0.97, 1.03], [0.5, 0.5], linewidth=1, color='blue')
plt.plot([1, 1], [0.2, 0.8], linewidth=1, color='blue')
plt.plot([0.97, 0.99], [0.75, 0.75], linewidth=1, color='red')
plt.plot([1.01, 1.03], [0.25, 0.25], linewidth=1, color='red')

plt.text(0.96, 0.67, f"f/f0 = {x1_param}", color='black', fontsize=8)
plt.text(0.96, 0.64, f"f/f0 = {x2_param}", color='black', fontsize=8)


plt.text(1.03, 0.33, f"f/f0 = {a1_param}", color='black', fontsize=8)
plt.text(1.03, 0.3, f"f/f0 = {a2_param}", color='black', fontsize=8)

plt.savefig('achkh.png')
