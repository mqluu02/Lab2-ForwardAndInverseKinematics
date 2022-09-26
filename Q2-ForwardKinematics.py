#!/usr/bin/env python3
from time import sleep
import sys
import math
import numpy as np 

#Define angles
theta1= 45 #degrees
theta2= 45 #degrees

theta1_rad= (theta1/180)*math.pi
theta2_rad= (theta2/180)*math.pi

#Define joint length
a1= 5
a2= 6
a3=5.5
a4=5


#Define H0_1 (concatenate to include [0 0 0 1] row at the end)
H0_1= [[math.cos(theta1_rad),-math.sin(theta1_rad),0,a2*math.cos(theta1_rad)],
        [math.sin(theta1_rad),math.cos(theta1_rad),0,a2*math.sin(theta1_rad)],
        [0, 0, 1, a1],
        [0, 0, 0, 1]]
#Define H1_2 (concatenate to include [0 0 0 1]row at the end)
H1_2= [[math.cos(theta2_rad),-math.sin(theta2_rad),0,a4*math.cos(theta2_rad)],
        [math.sin(theta2_rad),math.cos(theta2_rad),0,a4*math.cos(theta2_rad)],
        [0, 0, 1, a3],
        [0, 0, 0, 1]]
#H0_2=math.dot(H0_1,H1_2)
H0_2=np.dot(H0_1,H1_2)
print(H0_2)





