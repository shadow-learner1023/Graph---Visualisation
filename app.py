import sympy as sp
import numpy as np
import matplotlib.pyplot as plt



# DEFINE VARIABLE FOR LINE GRAPH
x=[float(i) for i in input("Enter the x values separated by commas : ").split(',')]
y=[float(i) for i in input("Enter the y values separated by commas : ").split(',')]

plt.plot(x,y)
plt.show()
