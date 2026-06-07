import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
print(np.__version__)

arr = np.array((1, 2, 3, 4, 5))
print(arr)

arr0D = np.array(42) # 0-D arrays or Scalars
print(arr0D)
arr1D = np.array([1, 2, 3, 4, 5]) # 1-D arrays, or uni-dimensional, is an array that has 5 0-D arrays as its elements
print(arr1D)
arr2D = np.array([[1, 2, 3], [4, 5, 6]]) # 2-D arrays is an array that has 1-D arrays as its elements
print(arr2D)
arr3D = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) # 3-D arrays with two 2-D arrays
print(arr3D)

print(arr0D.ndim)
print(arr1D.ndim)
print(arr2D.ndim)
print(arr3D.ndim)
arr5D = np.array([1, 2, 3, 4], ndmin=5)

print(arr5D)
print(f"Number of dimensions: {arr5D.ndim}")