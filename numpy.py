import numpy as np
print(np.zeros(10))
print(np.ones(10))
print(np.ones(10)*5)
print(np.arange(10,51))
print(np.arange(10,51,2)) #prints even numbers

#create 3 x 3 matrix
print(np.arange(9).reshape(3,3))

#create a 3 x 3 identity matrix
print(np.eye(3))

#use numpy to generate a random # btw 0 & 1
print(np.random.rand(3))

#random 25 #'s sampled from std. normal distr.
print(np.random.randn(5))
print(np.arange(1,101).reshape(10,10)/100)

#20 linearly spaced points
print(np.linspace(0,1,20))

mat = np.arange(1,26).reshape(5,5)
print(mat)