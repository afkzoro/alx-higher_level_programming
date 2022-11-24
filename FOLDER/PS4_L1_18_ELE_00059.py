# -*- coding: utf-8 -*-
"""
NAME:SAMUEL THEOPHILUS
REG NO:ENG/18/ELE/00059
DEPARTMENT:ELECTRICAL ENGINEERING
PROBLEM SET 4 L1

"""

import numpy as np
import  control as cnt
from matplotlib import pyplot as plt 

s=cnt.tf('s')
G1=5
G2=(s+0.1)*s
G3=(s+15)/(s+1000)
Kc=1 ; H=0.5
Gp=(Kc*G1*G3)/(1+G1*G2+Kc*G1*G3*H)

#%% This cell is for the original values of n and Ts
#From the plot the number of oscillations:7
n=7 #n is a variable for number of oscillations
P=np.pi
z=np.sqrt((4)/(n**2 * P**2 + 4))
#From the plot it is observed that the settling time is 80 seconds
Ts=112.5
Wn=(4)/(z*Ts)
print('Damping factor=',z)
print('Natural frequency=',Wn)
k=0.073

#Step Response for Gp
time=np.arange(0,200,0.1)
t1,y1=cnt.step_response(Gp,T=time)
#Step Response for Gs2
GS1=(k*Wn**2)/(s**2 + 2*z*Wn*s + Wn**2)
t2,y2=cnt.step_response(GS1,T=time)
plt.figure(1)
plt.plot(t1,y1,"k",linewidth =3,label="Figure Gp")#Gp is an under-damped response as observed from the plot
plt.plot(t2,y2,"b", linewidth=3,label="Figure GS1")
plt.grid()
plt.xlabel("Time(sec)")
plt.ylabel("response(y)")
plt.legend(loc="center right")
plt.show()


#%% This cell is for the adjusted values of n and Ts
n=5 #n is a variable for number of oscillations
P=np.pi 
z=np.sqrt((4)/(n**2 * P**2 + 4))
#From the plot it is observed that the settling time is 70 seconds
Ts=70
Wn=(4)/(z*Ts)
print('Damping factor=',z)
print('Natural frequency=',Wn)
k=0.073

#Step Response for Gp
time=np.arange(0,200,0.1)
t1,y1=cnt.step_response(Gp,T=time)
#Step Response for Gs2
GS2=(k*Wn**2)/(s**2 + 2*z*Wn*s + Wn**2)
t2,y2=cnt.step_response(GS2,T=time)
plt.figure(1)
plt.plot(t1,y1,"k",linewidth =2,label="Figure Gp")
plt.plot(t2,y2,"b", linewidth=2,label="Figure GS2")
plt.grid()
plt.xlabel("Time(sec)")
plt.ylabel("response(y)")
plt.legend(loc="center right")
plt.show()
#%%  QUESTION 11
#Inverse laplace of transform

#Input S-domain in the equation
import sympy
t, s = sympy.symbols('t,s')
a=sympy.symbols('a', real=True, positive=True)

GP1= (5*s**2 + 5075*s + 75000)/(5*(s**4) + 10000*(s**3) + 5001003.5*(s**2) + 504537.5*s + 1037500)

y=sympy.inverse_laplace_transform(GP1, s, t)
YS=sympy.laplace_transform(y,t,s, noconds=True)          
print('Partial Fraction=',GP1.apart(s))
print('y(t)=', y)
print()
