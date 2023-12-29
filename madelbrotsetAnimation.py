import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z**2 + c
        n += 1
    return n

def mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter):
    image = np.zeros((width, height))

    for x in range(width):
        for y in range(height):
            real = x_min + x * (x_max - x_min) / (width - 1)
            imag = y_min + y * (y_max - y_min) / (height - 1)
            c = complex(real, imag)
            color = mandelbrot(c, max_iter)
            image[x, y] = color

    return image

def update(frame):
    ax.clear()
    x_min, x_max = -2 + frame / 50, 2 - frame / 50
    y_min, y_max = -2 + frame / 50, 2 - frame / 50
    mandelbrot_image = mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter)
    ax.imshow(mandelbrot_image, cmap='hot', extent=(x_min, x_max, y_min, y_max))
    ax.set_title('Mandelbrot Set')
    ax.set_xlabel('Re')
    ax.set_ylabel('Im')

# Set the parameters
width = 800
height = 800
max_iter = 100

# Create a figure and axis
fig, ax = plt.subplots()

# Create the animation
animation = FuncAnimation(fig, update, frames=100, interval=50, repeat=False)

# Display the animation
plt.show()
