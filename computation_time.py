from SAW import *
from time import process_time
import matplotlib.pyplot as plt

N_max = 12
n = 10 #sample size per N
x=[]
y=[]
for N in range(N_max+1):
    s = SAW(N)
    for i in range(n):
        time1= process_time()
        print(s.possible_walks())
        time2= process_time()
        y.append(time2-time1)
        x.append(N)
        print(time2-time1)
#plt.yscale("log")
plt.scatter(x,y)
plt.show()
    
