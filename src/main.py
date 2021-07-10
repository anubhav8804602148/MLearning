import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt

#print(dir(plt))
x = [i for i in range(10)]
y = [i*i for i in range(10)]
print("plotting . . .")
plt.plot(x,y)
plt.show()