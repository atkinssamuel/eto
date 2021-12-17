import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1/(1 + np.exp(-x))


def third_deg_approx(x):
    a_0, a_1, a_3 = 0.5, 1.20096, -0.81562
    return a_0 + a_1 * x/8 + a_3 * np.power((x/8), 3)


def seven_deg_approx(x):
    b_0, b_1, b_3, b_5, b_7 = 0.5, 1.73496, -4.19407, 5.4302, -2.50739
    return b_0 + b_1 * x/8 + b_3 * np.power((x/8), 3) + b_5 * np.power((x/8), 5) + b_7 * np.power((x/8), 7)


def taylor_approx(x):
    c_0, c_1, c_3, c_5, c_7, c_9 = 1/2, 1/4, -1/48, 1/480, -17/80640, 31/1451520
    return c_0 + c_1 * x + c_3 * np.power(x, 3) + c_5 * np.power(x, 5) + c_7 * np.power(x, 7) * c_9 * np.power(x, 9)


x = np.arange(-8.1, 8.1, 0.1)
sig_y = sigmoid(x)
third_y = third_deg_approx(x)
seven_y = seven_deg_approx(x)
taylor_y = taylor_approx(x)

plt.plot(x, third_y, label="Third Degree Approx")
plt.plot(x, seven_y, label="Seventh Degree Approx")
plt.plot(x, taylor_y, label="Taylor Approx")
plt.plot(x, sig_y, label="Sigmoid")
plt.legend()
plt.ylim(-0.1, 1.1)
plt.grid()
plt.show()


print("Hello World")

