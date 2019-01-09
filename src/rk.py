import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def Lorentz(x,t):

    a=x[0]
    y=x[1]
    z=x[2]

    sigma=10.
    beta=8./3.
    rho=28.

    #defining the system of ODEs
    dxdt=sigma*(y-a)
    dydt= a*(rho-z)-y
    dzdt= a*y-beta*z


    return [dxdt,dydt,dzdt]


#Initial condtions
L=0.2 #20cm
m=0.3 #300g
g=9.8
x0=[1., 1., 1.]


#Time steps
tIn=0.
tFin=100.
h=0.05
totalSteps=int(np.floor((tFin-tIn)/h))
t=np.linspace(0,100,totalSteps)

x=odeint(Lorentz,x0,t)


a=x[:,0]
y=x[:,1]
z=x[:,2]


#Plotting
from pylab import meshgrid
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


fig=plt.figure()
ax=fig.gca(projection='3d')
ax.plot(a,y,z,'r',label='Lorentz Butterfly')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.legend()
fig.savefig('buterfly.pdf')
