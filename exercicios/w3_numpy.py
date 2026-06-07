import numpy as np # import numpy package

arr = np.array([1, 2, 3, 4, 5]) # 1-D array
print(arr)
print(type(arr))
print(np.__version__) # checking version

arr = np.array((1, 2, 3, 4, 5))
print(arr)

arr0D = np.array(42) # 0-D arrays or Scalars
print(arr0D)
arr1D = np.array([1, 2, 3, 4, 5]) # 1-D arrays, or uni-dimensional, is an array that has 5 0-D arrays as its elements
print(arr1D)
arr2D = np.array([[1, 2, 3], [4, 5, 6]]) # 2-D arrays is an array that has 1-D arrays as its elements
print(arr2D)
arr3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) # 3-D arrays with two 2-D arrays
print(arr3D)

print(arr0D.ndim)
print(arr1D.ndim)
print(arr2D.ndim)
print(arr3D.ndim)
arr5D = np.array([1, 2, 3, 4], ndmin=5) # create an array with 5 dimensions

print(arr5D)
print(f"Number of dimensions: {arr5D.ndim}")

print(arr[0]) # acessing 1-D array elements
print(arr2D[1, 2]) # acessing 2-D array elements
print(arr3D[1, 1, 2]) # acessing 3-D array elements
print(arr3D[1, 0, -1]) # negative indexing

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5]) # slice from index 1 to index 5
print(arr[4:]) # slice from index 4 to the end
print(arr[:4]) # slice from the beginning to index 4
print(arr[-3:-1]) # negative sliceing
print(arr[1:5:2]) # slice steping 2 from index 1 to index 5
print(arr[::2]) # slice steping 2 all array

arr2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr2d[1, 1:4]) # from the second element, slice from index 1 to index 4
print(arr2d[0:2, 2]) # from both elements return index 2
print(arr2d[0:2, 1:4]) # from both slice index 1 to index 4

print(arr2d.dtype) # type of the array
print(type(arr2d)) # type of variable
arrstr = np.array(["apple", "banana", "cherry"])
print(arrstr.dtype)
print(arrstr)

arr = np.array([1, 2, 3, 4], dtype="S")
print(arr)
print(arr.dtype)

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype("i")
print(newarr)
print(newarr.dtype)
newarr1 = arr.astype(int)
print(newarr1.dtype)

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(x)
print(arr)

y = arr.view()
arr[0] = 17
print(y)
print(arr)

z = arr.view()
z[0] = 111
print(z)
print(arr)

print(x.base)
print(y.base)
print(z.base)

print(arr3D.shape) # check the shape
print(arr.shape)
print(arr2d.shape)
print(arr5D.shape)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3) # reshape the array
print(newarr)
print(newarr.base)
newarr1 = arr.reshape(2, 3, 2)
print(newarr1)
newnew = newarr1.reshape(12)
print(newnew)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1) # 3D
print(newarr)
newarr1 = arr.reshape(-1, 4) # 2D # -1 allow the NumPy to decide this number for you
print(newarr1)
newarr2 = arr.reshape(-1) # flattening the arrays
print(newarr2)

arr1 = np.array([[[1, 2], [3, 4]],[[5, 6], [7, 8]]])
for i in np.nditer(arr1): # iterating
    print(i)

arr2 = np.array([1, 2, 3])
for i in np.nditer(arr2, flags=["buffered"], op_dtypes=["S"]):
    print(i)

arr3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for i in np.nditer(arr3[:, ::2]):
    print(i)

for idx, i in np.ndenumerate(arr):
    print(idx, i)

for idx, i in np.ndenumerate(arr3):
    print(idx, i)

# Join arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr3, arr4), axis=1)
print(arr)

arr = np.stack((arr1, arr2), axis=1)
print(arr)

arr = np.hstack((arr1, arr2))
print(arr)

arr = np.vstack((arr1, arr2))
print(arr)

arr = np.dstack((arr1, arr2))
print(arr)

# Split array
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

newarr = np.array_split(arr, 4)
print(newarr)

print(newarr[0])
print(newarr[1])
print(newarr[2])

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
print(arr)
newarr = np.array_split(arr, 3)
print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(arr)
newarr = np.array_split(arr, 3, axis=1)
print(newarr)

newarr = np.hsplit(arr, 3)
print(newarr)

newarr = np.vsplit(arr, 3)
print(newarr)

# Searching arrays

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

arr = np.array([10, 14, 93, 41, 8, 7])
x = np.where( arr % 2 == 1)
print(x)

arr = np.array([10, 14, 93, 41, 8, 7])
x = np.where(arr % 2 == 0)
print(x)

arr = np.array([6, 7, 7, 7, 7, 7, 8, 9])
x = np.searchsorted(arr, 7) # return the position where the number 7 is lower than the next number
print(x)

x = np.searchsorted(arr, 7, side="right")
print(x)

arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)

# Sort arrays

arr = np.array([3, 2, 0, 1])
arr1 = np.sort(arr)
print(arr)
print(arr1)

arr = np.array(["banana", "cherry", "apple"])
print(np.sort(arr))

arr = np.array([True, False, True])
print(np.sort(arr))

arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr)) # both arrays will be sorted

# Filtering arrays

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)

filter_arr = []
for i in arr:
    if i > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
print(filter_arr)
print(arr[filter_arr])
filter_arr = arr % 2 == 0
print(filter_arr)
print(arr[filter_arr])