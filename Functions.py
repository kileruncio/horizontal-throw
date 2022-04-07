
def analitic(x, y, t, g, xa_1, ya_1, vx, vy, a_x1, a_y1, dt):
    while y >= 0:
        xa_1.append(x)
        ya_1.append(y)

        vx_2 = vx + (a_x1*(dt/2))
        vy_2 = vy + (a_y1*(dt/2))

        x = vx*t
        y = vy*t-(g*pow(t, 2))/2
        t = t + dt

        if y > Max_Height_1:
            Max_Height_1 = y

    xa_1.append(x)
    ya_1.append(y)

while y >= 0:
    xa_1.append(x)
    ya_1.append(y)

    vx_2 = vx + (a_x1*(dt/2))
    vy_2 = vy + (a_y1*(dt/2))

    x = vx*t
    y = vy*t-(g*pow(t, 2))/2
    t = t + dt

    if y > Max_Height_1:
        Max_Height_1 = y

xa_1.append(x)
ya_1.append(y)