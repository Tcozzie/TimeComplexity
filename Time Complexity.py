import matplotlib.pyplot as plt
import numpy as np
import math

n=15
input_size=np.arange(n)

# LINEAR
count=0
while count<n:
    count+=1
print("Linear:", count)

# Plot It
linear=input_size*2
plt.plot(linear)

#QUADRATIC
count=0
for i  in  range(n):
    for j in range(n):
        count+=1
print("Quadratic:", count)
# Plot It
quadratic=linear**2
plt.plot(quadratic)

# CUBIC
count=0
for i  in  range(n):
    for j in range(n):
        for k in range(n):
            count+=1
print("Cubic:", count)

# Plot It
quadratic=linear**3
plt.plot(quadratic)


# EXPONENTIAL
count=1
def rec(n):
    global count
    if n>0:
        count+=1
        for i in range(2):
            rec(n-1)
rec(n)
print("Exp:",count)

# Plot It
exp=2**linear
plt.plot(exp)



plt.show()
