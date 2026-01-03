
import numpy as np
 
arr1d = np.ones(5)
print(arr1d)
# (Note the decimal points indicating float type)
arr2d = np.ones((3, 4))
print(arr2d)
 
# 1. Create a 1-dimensional array of 5 zeros (floats by default)
arr_1d = np.zeros(5)
print(f"1D Array: {arr_1d}")

# 2. Create a 2-dimensional array (2 rows, 3 columns)
arr_2d = np.zeros((2, 3))
print(f"\n2D Array:\n{arr_2d}")

#datatype of an array
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
 
#1D array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

#2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

#3D array
arr = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9],])
print(arr)

#dimensions the arrays have
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


 

# 1. Only stop provided: start=0, step=1
arr1 = np.arange(5)
print(f"One argument: {arr1}")

# 2. Start and stop provided: start=2, stop=8, step=1 (default)
arr2 = np.arange(2, 8)
print(f"Two arguments: {arr2}")

# 3. Start, stop, and step provided: start=1, stop=10, step=2
arr3 = np.arange(1, 10, 2)
print(f"Three arguments (step 2): {arr3}")

# 4. Floating-point numbers: start=0.5, stop=2.0, step=0.5
arr4 = np.arange(0.5, 2.0, 0.5)
print(f"Floating points: {arr4}")

# 5. Negative step to count backwards: start=5, stop=1, step=-1
arr5 = np.arange(5, 1, -1)
print(f"Counting backwards: {arr5}")
 
a = np.eye(3)
print(a)
# Creating a 3x3 identity matrix
b = np.eye(5)
print(b)
# Creating a 5x5 identity matrix

arr = np.linspace(0, 10, 5)
print(arr)
# Generate 5 evenly spaced numbers between 0 and 10 (inclusive)

 
arr = np.array([3, 1, 9, 2, 5])
minimum = np.min(arr)
maximum = np.max(arr)
print(f"Array: {arr}")
print(f"Minimum value: {minimum}")
print(f"Maximum value: {maximum}")

 
arr = np.array([3, 1, 9, 2, 5])

# Get the index of the minimum value (index of '1' is 1)
min_index = arr.argmin()

# Get the index of the maximum value (index of '9' is 2)
max_index = arr.argmax()

print(f"Array: {arr}")
print(f"Maximum value is: {arr[max_index]}")
print(f"Minimum value is: {arr[min_index]}")
print(f"Index of minimum value: {min_index}")
print(f"Index of maximum value: {max_index}")

 
arr = np.array([3,1,5,9,15,2,21,95])
min_index = arr.argmin()
max_index = arr.argmax()

print(f"Array: {arr}")
print(f"Maximum value is: {arr[max_index]}")
print(f"Minimum value is: {arr[min_index]}")
print(f"Index of minimum value: {min_index}")
print(f"Index of maximum value: {max_index}")
print(f"Sorted array: {np.sort(arr)}")
print(f"Sum of an  array: {np.sum(arr)}")
print(f"Mean of an  array: {np.mean(arr)}")
print(f"standard deviation of an  array: {np.std(arr)}")

 

# Create a 2x3 2D array
arr = np.array([[1, 2, 3],[4, 5, 6]])

print("2D array : \n" ,arr)

# Check the shape (rows, columns) and dimensions (ndim)
print("\nShape of an array is : ",arr.shape)
print("Dimensions of an array is : ",arr.ndim)

 

# Create a 2x3 2D array
arr = np.array([[1, 2, 3],[4, 5, 6]])
print("2D array : \n" ,arr)
first_row = arr[0, :]
print("\n Slicing  get the first row (index 0) : " , first_row)
second_col = arr[:, 1]
print("\n Slicing  get the second column (index 1) : " , second_col)

 

# Create a sample 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print("Original array:\n", arr)

total_sum = arr.sum()
print(f"Sum of all elements: {total_sum}")

column_sums = arr.sum(axis=0)
print(f"Sum along columns: {column_sums}")

row_sums = arr.sum(axis=1)
print(f"Sum along rows: {row_sums}")

 
#Slicing 1D Arrays

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print("Array is : ",arr)
print("Elements from index 1 up to (but not including) index 6 : ",arr[1:6])
print("Elements from the beginning to index 5 (exclusive) : ",arr[:5])
print("Elements from index 5 to the end : ",arr[5:])

#Slicing 2D Arrays
 
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])
print("Original matrix:\n", matrix)
print("Select all elements in the second row : ",matrix[1, :])
print("Select all elements in the third column : ",matrix[:, 2])
print("Select a submatrix (first two rows, first three columns) : \n" ,matrix[:2, :3])

 

matrix1 = np.array([[15, 25, 30, 41],
                   [56, 65, 70, 82]])

matrix2=np.array([[12,15,2],[20,1,9]])
print("The matrix 1 is : \n",matrix1)

print("\nThe matrix 2 is : \n",matrix2)

slice_arr=matrix1[:2,:2]
print("\nThe sliced array is : \n",slice_arr)

matrix1_slice = matrix1[:2,:3]
print("\nThe sliced array is : \n",matrix1_slice)

print("\nThe matrix 2 is : \n",matrix2)

print("\nThe Addition is : \n",np.add(matrix1_slice,matrix2))
print("\nThe Subtraction is : \n",np.subtract(matrix1_slice,matrix2))
print("\nThe Modulus is : \n",np.mod(matrix1_slice,matrix2))
print("\nThe Remainder is : \n",np.remainder(matrix1_slice,matrix2))
print("\nThe Multiplication is : \n",np.multiply(matrix1_slice,matrix2))
print("\nThe Division is : \n",np.divide(matrix1_slice,matrix2))
print("\nThe Power is : \n",np.power(matrix1_slice,matrix2))
print("\nThe Absolute is : \n",np.absolute(matrix1_slice,matrix2))

index_arr=matrix1[[1,1],[2,1]]
print("\nThe index array is : ",index_arr)
print("\nThe Sum  is :",matrix1.sum())

 

arr= np.array([[4, 9, 16],[81, 121, 225]])
print("The array is : \n",arr)
result = np.sqrt(arr)
print("\nThe Square root of number is :\n",result)

 

# Original 2D array (3 rows, 2 columns)
arr = np.array([[1, 2],
                [3, 4],
                [5, 6]])

transposed_arr = arr.T

print("Original array:")
print(arr)
print("\nTransposed array using .T:")
print(transposed_arr)

 

A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

result_dot = np.dot(A, B)


print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nResult of np.dot(A, B) :")
print(result_dot)
# Result[0, 0] (top-left element):
# (1 * 7) + (2 * 9) + (3 * 11) = 7 + 18 + 33 = 58
# Result[0, 1] (top-right element):
# (1 * 8) + (2 * 10) + (3 * 12) = 8 + 20 + 36 = 64
# Result[1, 0] (bottom-left element):
# (4 * 7) + (5 * 9) + (6 * 11) = 28 + 45 + 66 = 139
# Result[1, 1] (bottom-right element):
# (4 * 8) + (5 * 10) + (6 * 12) = 32 + 50 + 72 = 154

 

# Create a 2D array of booleans
arr = np.array([[True,True], [False, True]])

print(arr)
print(arr.dtype)
print(arr.ndim)
print(arr.shape)
print(np.all(arr))
print(np.any(arr))

 

# Creating a sequence of numbers from 0 to 9
sequence1 = np.arange(10)
print("Basic Sequence:", sequence1)

# Creating a sequence of floating-point numbers from 0 to 1 with a step size of 0.2 using np.arange()
sequence2 = np.arange(0, 1, 0.2)
print("Floating-Point Sequence:", sequence2)

 

# Create a 1D array with 12 elements
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(f"Original array: {arr}")
print("1D to 2D : \n",arr.reshape(3, 4))

 
a = np.array([[1, 2],[4, 3]])
b = np.array([[10, 21],[40, 35]])
c = np.array([[11, 32],[54, 13]])
print("The array 1 is : \n",a)
print("\nThe array 2 is : \n",b)
print("\nThe array 3 is : \n",c)

d = np.vstack((a,b,c))
print("\nThe Vertical stack is : \n",d)
e= np.hstack((a,b,c))
print("\nThe Horizontal stack is : \n",e)

 
arr = np.array([[1, 2, 4, 3],[10, 21, 40, 35]])
print("The array  is : \n",arr)

a=np.hsplit(arr,2)
print("\nThe Horizontal split is : \n",a)
b=np.vsplit(arr,2)
print("\nThe Vertical split is : \n",b)

 

x = np.array([10, 25, 39, 49, 225])

# Print results
print("Array:", x)
print("Square root:", np.sqrt(x))
print("Exponential:", np.exp(x))
print("Sine:", np.sin(x))
print("Cosine:", np.cos(x))
print("Log:", np.log(x))
print("Sum:", np.sum(x))
print("Standard Deviation:", np.std(x))

 

# 1. random.rand() → random floats in [0, 1)
rand_values = np.random.rand(5)
print("Random floats (rand):", rand_values)

# 2. random.randint() → random integers
rand_ints = np.random.randint(1, 10, size=5)
print("Random integers (randint):", rand_ints)

# 3. random.permutation() → random permutation
perm = np.random.permutation(5)
print("Permutation of numbers 0–4:", perm)

# Permutation of an array
arr = np.array([10, 20, 30, 40, 50])
perm_arr = np.random.permutation(arr)
print("Permutation of array:", perm_arr)

# 4. random.random() → random floats (similar to rand)
random_values = np.random.random(5)
print("Random floats (random):", random_values)

 


#   random.random() → random float numbers between 0.0 and 1.0
r = np.random.random(5)
print("Random values:", r)

#  random.rand() → random floats in [0, 1)
rand_values = np.random.rand(5)
print("Random floats (rand):", rand_values)

# 2. random.randint() → random integers
rand_ints = np.random.randint(1, 10, size=5)
print("Random integers (randint):", rand_ints)

# 3. random.permutation() → random permutation
perm = np.random.permutation(5)
print("Permutation of numbers 0–4:", perm)

# Permutation of an array
arr = np.array([10, 20, 30, 40, 50])
perm_arr = np.random.permutation(arr)
print("Permutation of array:", perm_arr)

# 4. random.random() → random floats (similar to rand)
random_values = np.random.random(5)
print("Random floats (random):", random_values)