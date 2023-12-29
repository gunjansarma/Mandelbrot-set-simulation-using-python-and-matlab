import numpy as np
import matplotlib.pyplot as plt

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

def plot_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    mandelbrot_image = mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter)

    plt.imshow(mandelbrot_image, cmap='hot', extent=(x_min, x_max, y_min, y_max))
    plt.colorbar()
    plt.title('Mandelbrot Set')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.show()

# Set the parameters
width = 800
height = 800
x_min, x_max = -2, 2
y_min, y_max = -2, 2
max_iter = 100

# Plot the Mandelbrot set
plot_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)
