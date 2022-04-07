from math import sin, cos, radians
import matplotlib.pyplot as plt
import numpy as np


theta = radians(float(input("Enter Initial Launch Angle of the Object from 0 Degree to 360 Degree: ")))
dt = 0.01                                                           # The delta time step of the motion
v = float(input("Enter Launch velocity in (m/s): "))                # Launch velocity
g = 9.81                                                            # Gravitational Acceleration
k = float(input("Enter Resistance Force Consant: "))                # Resistance force constant
m = float(input("Enter Mass of the object in(kg): "))               # Mass of the object
t = 0.0                                                             #Starting time
x = 0.0
y = 0.0
vx,vy = v*cos(theta), v*sin(theta)  # Initial vertical and horizontal speeds
a_x0 = 0.0                          # Horizontal forces without drag force case.
a_x1 = -(k*vx)/m                    # Horizontal forces with drag force case.
a_y0 = -g                           # Only gravitational force.
a_y1 = (-g-(k*vy)/m)                # Both drag force and gravitational force.
Max_Height_0 = 0.0                  # Maximum Height,initially set to zero
Max_Height_1 = 0.0                  # Maximum Height,initially set to zero
xa_1 = list()
ya_1 = list()
xa_2 = list()
ya_2 = list()
xa_3 = list()
ya_3 = list()


while y >= 0: #Follow the ball while it hasn't gone below the y position of its initial position
     xa_2.append(x)		     # add x to the x array
     ya_2.append(y)          # add y to the y array
     
     vx_2 = vx + (a_x0*(dt/2))
     vy_2 = vy + (a_y0*(dt/2))

     y = y + vy_2 * dt        
     x = x + vx_2 * dt
     vy = vy + a_y0 * dt
     vx = vx + a_x0 * dt
     t = t + dt             #Step up the time
     if y > Max_Height_0:   #Update the value of the Maximum Height whenever a larger value of y is found
          Max_Height_0 = y 
# =============================================================================
xa_2.append(x)		    # add x to the x array
ya_2.append(y)         # add y to the y array


# RE-CONFIG
vx,vy = v*cos(theta), v*sin(theta) #Initial vertical and horizontal speeds
t = 0.0 #Starting time
x = 0.0
y = 0.0


# ITERATIVE ALGORITHM USING EULER'S METHOD FOR MOTION WITH DRAG FORCE
# =============================================================================
while y >= 0:               #Follow the ball while it hasn't gone below the y position of its initial position
     xa_3.append(x)		     # add x to the x array
     ya_3.append(y)          # add y to the y array

     
     # Since only velocity can change by time, we do not need to find acceleration for (dt/2) in case of w/o drag force
     vx_2 = vx + (a_x1*(dt/2))
     vy_2 = vy + (a_y1*(dt/2))


     # Use Euler's algorithm
     y = y + vy_2 * dt        
     x = x + vx_2 * dt
     vy = vy + a_y1 * dt
     vx = vx + a_x1 * dt
     t = t + dt             #Step up the time
     if y > Max_Height_1:   #Update the value of the Maximum Height whenever a larger value of y is found
          Max_Height_1 = y 
# =============================================================================
xa_3.append(x)		    # add x to the x array
ya_3.append(y)          # add y to the y array

# RE-CONFIG
vx,vy = v*cos(theta), v*sin(theta) #Initial vertical and horizontal speeds
t = 0.0 #Starting time
x = 0.0
y = 0.0

while y >= 0:
     xa_1.append(x)		     # add x to the x array
     ya_1.append(y)           # add y to the y array

     
     # Since only velocity can change by time, we do not need to find acceleration for (dt/2) in case of w/o drag force
     vx_2 = vx + (a_x1*(dt/2))
     vy_2 = vy + (a_y1*(dt/2))

     
     vy = vy - dt*(k/m)*np.sqrt(vx**2+vy**2)*vy + g
     vx = vx - dt*(k/m)*np.sqrt(vx**2+vy**2)*vx
     y = ya_1[-1] + vy_2
     x = xa_1[-1] + vx_2
     t = t + dt             #Step up the time
     if y > Max_Height_1:   #Update the value of the Maximum Height whenever a larger value of y is found
          Max_Height_1 = y 

xa_1.append(x)
ya_1.append(y)


plt.figure()
plt.plot(xa_2, ya_2, color = 'r', label = "Analitic")
plt.plot(xa_3, ya_3, color = 'g', label = "Mid-point")
plt.ylim(0, Max_Height_0+Max_Height_0/10)
plt.ylabel('Horizontal Axis (m)')
plt.xlabel('Vertical Axis (m)')
plt.title('Trajectory Motion of Object')
plt.legend()
plt.show()