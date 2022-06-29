import numpy as np
import matplotlib.pyplot as plt

dx = 0.01
x = np.arange(-5.0, 10.0, dx)

# def f(x):
#     return 0.1*x**3 - 0.5*x**2 - 5*x +10

f = np.poly1d([0.1, -0.5, -5.0, 10])
y = f(x)
plt.plot(x,y, label="$f(x)=0.1x^3-0.5x^2-5x+10$", color='g')

# derivative 
derivative = f.deriv()
yd = derivative(x)
plt.plot(x,yd, label=derivative, color='r')

  # partial derivative
x1        = [8.0-dx, 8.0, 8.0+dx]
y1        = f(x1)
slope     = (y1[-1] - y1[0] ) / (x1[-1] - x1[0])
intercept = y1[0] - slope * x1[0]
partial_derivative = np.poly1d ([slope, intercept])
x_partial_derivative = np.linspace(7, 10, 100)
y_partial_derivative = partial_derivative(x_partial_derivative)
plt.plot(x_partial_derivative,y_partial_derivative, color="y",label=partial_derivative)

# integration
xi = np.arange(-4.0, 0.0+0.5, 0.5)
for i in range (len(xi)-1): # to handle the last element
    xs = [xi[i],   xi[i] ,   xi[i+1] , xi[i+1]   ]
    ys = [0    , f(xi[i]), f(xi[i+1]), 0]
    plt.fill(xs,ys,color='b',edgecolor='k',alpha=0.2)
area = np.trapz(f(xi), xi)

text_box_string = "$\int_{-4}^0 f(x)dx =$" + f"{area}"
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
plt.text(-4,-7, text_box_string, fontsize=10, bbox=props)

plt.grid()
plt.xlabel("x [unit]")
plt.ylabel("y [unit]")
plt.title("Example")
plt.legend(loc="upper right")
plt.show()