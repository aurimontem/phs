#!/usr/bin/env python3
# '#!' - tells shell to run the program using python3

# you can import modules in a script
import math

print('PART A')
# range(3) effectively returns [0, 1, 2]
for i in range(5):
    print(i)


print('PART B')
times = [0, 1, 3, 5, 6, 7]
distances = [0, 4, 7, 10, 11, 12]
velocities = []
# why do we only go to len(distances) - 1?
for i in range(len(distances) - 1):
    velocity = (distances[i+1] - distances[i])/(times[i+1] - times[i])
    velocities.append(velocity)
print(velocities)


print('PART C')
# in python, if you don't properly indent you will get an error
def simple_loop(beginning, end):
    total = 0
    # range is exclusive of end - range(1,3) produces [1,2]
    for elem in range(beginning, end):
        total += elem
    print("Sum from",beginning,"to",end-1,"is",total)

simple_loop(3, 14)

run_part_d = False 
if run_part_d:
    print('PART D')
    import numpy as np
    import scipy.integrate
    import matplotlib.pyplot as plt

    def integrand(x, t):
        # dx/dt = my_integrand
        my_integrand = 5*x - x**2
        return my_integrand

    t = np.linspace(0, 5, 21) # make a grid of 11 points that go 0,1,2,...,10
    x0 = .2 # choose an initial condition
    # integrate the function integrand, with initial condition x0, over times t:
    y = scipy.integrate.odeint(integrand, x0, t)
    # print the output (solution) of the differential equation:
    print(y)

    plt.plot(t, y, '.')
    plt.savefig('my_first_figure.pdf')

