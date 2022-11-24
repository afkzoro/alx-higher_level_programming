"""
NAME:SAMUEL THEOPHILUS
REG NO:ENG/18/ELE/00059
DEPARTMENT:ELECTRICAL ENGINEERING
PROBLEM SET 4 L2
"""
import numpy as np
import control as cnt
from matplotlib import pyplot as plt
s=cnt.tf('s')
k = 0.073
Wn =0.452422152534405
z = 0.12630428643414326
#Controller Gains

Kp = 4; Ki = 5.5; Kd = 10
Kc1= Kp + Kd*s + Ki/s 


GS2=(k*Wn**2)/(s**2 + 2*z*Wn*s + Wn**2)
Gcl1 = cnt.feedback(GS2*Kc1, 1)


G1=5
G2=(s+0.1)*s
G3=(s+15)/(s+1000)
Kc=1 ; H=0.5
Gp=(Kc*G1*G3)/(1+G1*G2+Kc*G1*G3*H)
Gcl2 = cnt.feedback(Gp*Kc1, 1)

time=np.arange(0,50,0.1)
t1,y1=cnt.step_response(Gcl1,T=time)
t2,y2=cnt.step_response(Gcl2,T=time)

plt.figure(1)
plt.plot(t1,y1, linewidth = 2, color = 'k', label = 'Figure Gcl1')
plt.plot(t2,y2, linewidth = 2, color = 'r', label = 'Figure Gcl2')
plt.grid()
plt.xlabel("Time(sec)")
plt.ylabel("response(y)")
plt.legend(loc="center right")
plt.show()


