import numpy as np
#  A random vector  is generated  of size 20 with float numbers between 1 and 20
Random_Vector = np.random.uniform(1, 20, 20)


# Reshape the array to 4 by 5
Reshaped_Vector = Random_Vector.reshape(4, 5)
print(" array after reshaping to (4,5) \n")
print(Reshaped_Vector)

# The  maximum value in each row is found
max_values = np.argmax(Reshaped_Vector, axis=1)
print("\n")
# The maximum value in each row is replaced with 0
Reshaped_Vector[np.arange(Reshaped_Vector.shape[0]), max_values] = 0
print(" replacing the maximum value in each row with 0  \n")
print(Reshaped_Vector)