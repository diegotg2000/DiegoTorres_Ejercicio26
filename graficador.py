import numpy as np
import matplotlib.pyplot as plt



t=np.loadtxt('explicito.txt',usecols=0)
Y_e=np.loadtxt('explicito.txt',usecols=1)
Y_r=np.loadtxt('rk4.txt',usecols=1)
Y_lf=np.loadtxt('lf.txt',usecols=1)
V_e=np.loadtxt('explicito.txt',usecols=2)
V_r=np.loadtxt('rk4.txt',usecols=2)
V_lf=np.loadtxt('lf.txt',usecols=2)

plt.figure(figsize=(10,10))
plt.subplot(3,3,1)
plt.plot(t, Y_e)
plt.xlim((0,4*np.pi))
plt.ylim((-1.5,1.5))
plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Euler')
plt.subplot(3,3,2)
plt.plot(t, Y_r)
plt.xlim((0,4*np.pi))
plt.ylim((-1.5,1.5))
plt.xlabel('Time')
plt.title('RK')
plt.subplot(3,3,3)
plt.plot(t, Y_lf)
plt.xlim((0,4*np.pi))
plt.ylim((-1.5,1.5))
plt.xlabel('Time')
plt.title('Leap Frog')
plt.subplot(3,3,4)
plt.plot(t, V_e)
plt.xlim((0,4*np.pi))
plt.ylim((-1.5,1.5))
plt.xlabel('Time')
plt.ylabel('Velocity')
plt.subplot(3,3,5)
plt.plot(t, V_r)
plt.xlim((0,4*np.pi))
plt.ylim((-1.5,1.5))
plt.xlabel('Time')
plt.subplot(3,3,6)
plt.plot(t, V_lf)
plt.xlim((0,4*np.pi))
plt.ylim((-1.5,1.5))
plt.xlabel('Time')
plt.subplot(3,3,7)
plt.plot(Y_e, V_e)
plt.xlim((-2,2))
plt.ylim((-2,2))
plt.xlabel('Position')
plt.ylabel('Velocity')
plt.subplot(3,3,8)
plt.plot(Y_r, V_r)
plt.xlim((-2,2))
plt.ylim((-2,2))
plt.xlabel('Position')
plt.subplot(3,3,9)
plt.plot(Y_lf, V_lf)
plt.xlim((-2,2))
plt.ylim((-2,2))
plt.xlabel('Position')

plt.savefig('graficas.png')