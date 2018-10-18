#!/usr/bin/python
# '#!' - tells shell to run the program using python, located in /bin/python.
# (replace this path with yours by running 'whereis python' in the shell)

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

print('PART D: FIND THE ERROR')
print()
new_var = my_new_variable + 14
print(new_var)
