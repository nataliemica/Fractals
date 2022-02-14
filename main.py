import pyximport; pyximport.install()
import fractal

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import time

start = time.time()

def zoom_animate(i):
    x_start_zoom, y_start_zoom = 1.1**(-i)*x_start+x_center, 1.1**(-i)*y_start+y_center
    width_zoom, height_zoom = 1.1**(-i)*width, 1.1**(-i)*height
    
    real_zoom = np.linspace(x_start_zoom, x_start_zoom+width_zoom, density)
    imag_zoom = np.linspace(y_start_zoom, y_start_zoom+height_zoom, density)
    
    axes.clear()
    axes.set_xticks([],[])
    axes.set_yticks([],[])
    X_zoom = np.empty((len(real_zoom),len(imag_zoom)))
    
    for i in range(len(real_zoom)):
        for j in range(len(imag_zoom)):
            X_zoom[i,j] = fractal.mandelbrot(real_zoom[i],imag_zoom[j],60)
            
    img = axes.imshow(X_zoom.T, cmap='hsv')
    return [img]

x_center, y_center = -0.761574,-0.0847596
x_start, y_start = -1.75,-1.5
width, height = 3,3
density = 100
    
real_axis = np.linspace(x_start, x_start+width, density)
imag_axis = np.linspace(y_start, y_start+height, density)
    
fig = plt.figure(figsize=(7,7))
axes = plt.axes()

my_anim = animation.FuncAnimation(fig, zoom_animate, frames=80, interval=100, blit=True)
my_anim.save('mandelbrot_zoom.gif',writer='imagemagick')
    
duration = time.time()-start
print("Time spent: ",duration)
