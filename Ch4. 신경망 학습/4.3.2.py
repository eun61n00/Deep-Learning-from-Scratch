def function_1(x):
    return 0.01*x**2 + 0.1*x
  
import numpy as np
import matplotlib.pylab as plt

x = np.arange(0.0, 20.0, 0.1) #0에서 20까지 0.1간격의 배열 x를 만든다.
y = function_1(x)
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y)
plt.show

numerical_diff(function_1, 5)
numerical_diff(function_1, 10)

def tangent_line(f, x):
    d = numerical_diff(f, x)
    print(d)
    y = f(x) - d*x
    return lambda t: d*t + y
     
x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")

tf = tangent_line(function_1, 5)
y2 = tf(x)

plt.plot(x, y)
plt.plot(x, y2)
plt.show()

tf2 = tangent_line(function_1, 10)
y3 = tf2(x)

plt.plot(x, y)
plt.plot(x, y3)
plt.show()
