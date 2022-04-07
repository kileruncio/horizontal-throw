import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math, sys

#kontrola poprawności argumentu
try:
	if len(sys.argv) != 3: raise Exception('Zła ilość argumentów')
	if not 0 <= float(sys.argv[1]) <= 90: raise Exception('Za duża lub za mała wartość kąta. Kąt musi być między 0 a 90 stopni.')
	angle = math.radians(float(sys.argv[1]))
	if not 5 <= float(sys.argv[2]) <= 50: raise Exception('Prędkość musi zawierać się między 5 a 50.')
	v = float(sys.argv[2])
except Exception as e:
	print("Proszę podać dokładnie dwa argumenty, gdzie pierwszy jest wartością kąta w stopniach, a drugi prędkośćią.\n")
	print(e)
	sys.exit()

#zmienne
r = 0.2 # promień kuli, np. rzucanej piłki
kappa = 0.45 *np.pi * r*r * 0.6 #współczynnik oporu powietrza
m = 0.3 # masa kuli
g = 9.81 #przyśpieszenie ziemskie
t = 0.1 #wielkosc kroku dla schematu eulera

#wartości poćżątkowe
x = [0,]
y = [0,]
vx = [v*math.cos(angle),]
vy = [v*math.sin(angle),]

#kolejne iteracje dla schematu eulera
while not y[-1] < 0:
	vx.append(vx[-1] -  t*(kappa/m)*np.sqrt( vx[-1]**2 + vy[-1]**2)*vx[-1]   )
	vy.append(vy[-1] -  t*( (kappa/m)*np.sqrt( vx[-1]**2 + vy[-1]**2)*vy[-1] + g)  )
	x.append(x[-1] +  vx[-2])
	y.append(y[-1] +  vy[-2])

def animate(t):
	line = ax.plot(x[0:t], y[0:t], color = 'b')
	return line

fig, ax = plt.subplots()

scale_len = int(1.4 * max (x + y))
ax.set_xlim(0, scale_len)
ax.set_ylim(0, scale_len)

ani = animation.FuncAnimation(fig, animate, interval=80, blit=True)
plt.show()