from math import sin, cos, radians
import matplotlib.pyplot as plt

name = input('''Choose an option:
m - solveMid-Point
e - solveEuler
''')
theta = radians(float(input("Enter Initial Launch Angle of the Object from 0 Degree to 360 Degree: ")))
DT = 0.01                                                           # The delta time step of the motion
v = float(input("Enter Launch velocity in (m/s): "))                # Launch velocity
G = -9.81                                                           # Gravitational Acceleration
k = float(input("Enter Resistance Force Consant: "))                # Resistance force constant
m = float(input("Enter Mass of the object in(kg): "))               # Mass of the object
t = 0.0                                                             #Starting time
x = 0.0
y = 0.0
vx,vy = v*cos(theta), v*sin(theta)  # Initial vertical and horizontal speeds
a_x1 = -(k*vx)/m                    # Horizontal forces with drag force case.
a_y1 = (G-(k*vy)/m)                 # Both drag force and gravitational force.
Max_Height = 0.0                    # Maximum Height,initially set to zero
xa_1 = list()
ya_1 = list()
xa_2 = list()
ya_2 = list()
xa_3 = list()
ya_3 = list()

def euler(y, x, t, vx, vy, xa_1, ya_1, Max_Height):
     while y >= 0: 
          xa_1.append(x)
          ya_1.append(y)

          y = y + vy * DT        
          x = x + vx * DT
          vy = vy + a_y1 * DT
          vx = vx + a_x1 * DT
          t = t + DT
          if y > Max_Height:
               Max_Height = y 

     xa_1.append(x)
     ya_1.append(y)

     return Max_Height

def analitical(y, x, t, vx, vy, xa_2, ya_2, Max_Height):
     while y >= 0: 
          xa_2.append(x)
          ya_2.append(y)       
          
          vx_2 = vx + G*0.5*t*t*DT
          vy_2 = vy + G*0.5*t*t*DT

          y += vy_2 * DT
          x += vx_2 * DT
          vy = vy + a_y1 * DT
          vx = vx + a_x1 * DT
          t += DT
          if y > Max_Height:
               Max_Height = y 
          
     xa_2.append(x)
     ya_2.append(y)

     return Max_Height


def mid_point(y, x, t, vx, vy, xa_3, ya_3, Max_Height):
     while y >= 0:
          xa_3.append(x)
          ya_3.append(y)
               
          vx_2 = vx + (a_x1*(DT/2))
          vy_2 = vy + (a_y1*(DT/2))

          y = y + vy_2 * DT
          x = x + vx_2 * DT
          vy = vy + a_y1 * DT
          vx = vx + a_x1 * DT
          t = t + DT
          if y > Max_Height:
               Max_Height = y 
         
     xa_3.append(x)
     ya_3.append(y)

     return Max_Height

if name == 'm':
     h1 = analitical(y, x, t, vx, vy, xa_1, ya_1, Max_Height)
     h0 = mid_point(y, x, t, vx, vy, xa_3, ya_3, Max_Height)
     

     if h1 > h0:
          Max_Height = h1 
     else:
          Max_Height = h0
elif name == 'e':
     h1 = analitical(y, x, t, vx, vy, xa_1, ya_1, Max_Height)
     h0 = euler(y, x, t, vx, vy, xa_2, ya_2, Max_Height)
     

     if h1 > h0:
          Max_Height = h1 
     else:
          Max_Height = h0
elif name == 'all':
     h1 = analitical(y, x, t, vx, vy, xa_1, ya_1, Max_Height)
     h2 = mid_point(y, x, t, vx, vy, xa_3, ya_3, Max_Height)
     h0 = euler(y, x, t, vx, vy, xa_2, ya_2, Max_Height)

     if h0 > h1 and h0 > h2:
          Max_Height = h0
     elif h0 <= h1 and h0 >= h2:
          Max_Height = h1
     else:
          Max_Height = h2
else:
     print('Bad argument')

plt.figure()
plt.plot(xa_1, ya_1, color = 'r', label = 'Analitic')  #Analitic
plt.plot(xa_2, ya_2, color = 'b', label = 'Euler')     #Euler
plt.plot(xa_3, ya_3, color = 'g', label = 'Mid-Point') #Mid-Point
plt.ylim(0, Max_Height + Max_Height/10)
plt.ylabel('Horizontal Axis (m)')
plt.xlabel('Vertical Axis (m)')
plt.title('Trajectory Motion of Object')
plt.show()