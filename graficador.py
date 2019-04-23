import numpy as np
import matplotlib.pyplot as plt



t=np.loadtxt('explicito.txt',usecols=0)
Y_e=np.loadtxt('explicito.txt',usecols=1)
Y_r=np.loadtxt('rk4.txt',usecols=1)


plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.plot(t, Y_e)
plt.title('Euler explícito')
plt.subplot(1,2,2)
t=np.loadtxt('rk4.txt',usecols=0)
plt.plot(t, Y_r)
plt.title('Runge-Kutta')
plt.savefig('graficas.png')