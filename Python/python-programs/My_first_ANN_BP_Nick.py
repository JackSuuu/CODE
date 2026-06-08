from mpl_toolkits.mplot3d import axes3d
from matplotlib import pyplot as plt
import numpy as np
import os

# The data [day, time, type(1 = many people, 0 = not many people)]

data = [
    [1, 7, 1],
    [1, 7.5, 1],
    [1, 8, 1],
    [2, 7.1, 1],
    [2, 7.4, 1],
    [2, 8, 1],
    [3, 8, 1],
    [3, 7.6, 1],
    [4, 7.7, 1], 
    [5, 9.2, 1],
    [1, 6.4, 0],
    [2, 7, 0],
    [2, 6.7, 0],
    [3, 7.4, 0],
    [3, 7, 0],
    [4, 8, 0],
    [4, 6.5, 0],
    [5, 7.5, 0],
    [5, 7.6, 0],
]

# Super simple neural network !
# Initialize weights and bias randomly
w1 = np.random.randn()
w2 = np.random.randn()
b = np.random.randn()

# Activation functions, we try sigmoid function first
# Sigmoid


def sigmoid(x):
    return 1/(1 + np.exp(-x))


def dsigmoid(x):
    return sigmoid(x) * (1-sigmoid(x))
# ReLU


def ReLU(x):  # does not specify the ReLU activation in network
    return x * (x > 0)


def dReLU(x):  # does not specify the ReLU activation in network
    return 1. * (x > 0)
# Softmax for the output layer


def softmax(x, axis=None):  # The ANN does not using softmax at all
    x = x - x.max(axis=axis, keepdims=True)
    y = np.exp(x)
    return y / y.sum(axis=axis, keepdims=True)


# Scatter diagram for points
for i in range(len(data)):
    point = data[i]
    color = "r"
    if point[2] == 0:
        color = "b"
    plt.scatter(point[0], point[1], c=color)
plt.show()

# Plotting 3D model of the cost function for every point
z = 0
for j in range(len(data)):
    n = 1000
    x, y = np.meshgrid(np.linspace(-3, 3, n),
                       np.linspace(-3, 3, n))
    learning_rate = 0.3
    # Forward propagation
    point = data[j]
    target = point[2]
    z = np.square((point[0] * x + point[1] * y + b) - target) + z

plt.figure('Surface', facecolor='lightgray')
ax3d = plt.gca(projection='3d')
ax3d.set_xlabel('X', fontsize=14)
ax3d.set_ylabel('Y', fontsize=14)
ax3d.set_zlabel('Z', fontsize=14)
ax3d.plot_surface(x, y, z, rstride=50, cstride=50, cmap='jet')
plt.show()


costs = []
# Training iteration
for i in range(100000):  # The model only has one unit
    learning_rate = 0.1
    # Pick a random point, or else it might be biased
    random_index = np.random.randint(len(data))
    point = data[random_index]
    # Forward propagation
    y = point[0] * w1 + point[1] * w2 + b
    prediction = sigmoid(y)
    target = point[2]
    cost = np.square(prediction - target)  # why MSE for sigmoid activation?
    # Back propagation
    # Consider partial derivatives
    # Differentiate cost w.r.t prediction
    dcost_dprediction = 2 * (prediction - target)
    # Differentiate prediciton w.r.t to y
    dprediction_dy = dsigmoid(y)
    # Differentiate y w.r.t w1
    dy_dw1 = point[0]
    # Differentiate y w.r.t w2
    dy_dw2 = point[1]
    # Differentiate y w.r.t b
    dy_db = 1
    # Using chain rule
    dcost_dw1 = dcost_dprediction * dprediction_dy * dy_dw1
    dcost_dw2 = dcost_dprediction * dprediction_dy * dy_dw2
    dcost_db = dcost_dprediction * dprediction_dy * dy_db
    # Gradient descent
    w1 = w1 - learning_rate * dcost_dw1
    w2 = w2 - learning_rate * dcost_dw2
    b = b - learning_rate * dcost_db

    if i % 100 == 0:
        costs.append(cost)

# Costs decreasing graph
plt.plot(costs)
plt.show()

day = float(input("Please enter a day:"))
time = float(input("Please enter a time:"))
y = day * w1 + time * w2 + b
prediction = sigmoid(y)
print(prediction)
if prediction > 0.5:
    os.system("say 很多人")
else:
    os.system("say 没有很多人")
