import numpy as np
import time

print("=" * 60)
print("           NUMPY DATA EXPLORER")
print("=" * 60)

# ---------------------------------------------------------
# 1. ARRAY CREATION
# ---------------------------------------------------------

print("\n1. ARRAY CREATION")

arr = np.array([10, 20, 30, 40, 50])
print("Basic Array:", arr)

zeros = np.zeros(5)
print("Zeros Array:", zeros)

ones = np.ones(5)
print("Ones Array:", ones)

range_array = np.arange(1, 11)
print("Range Array:", range_array)


# ---------------------------------------------------------
# 2. INDEXING AND SLICING
# ---------------------------------------------------------

print("\n2. INDEXING AND SLICING")

print("Original Array:", arr)

print("First Element:", arr[0])
print("Third Element:", arr[2])
print("Last Element:", arr[-1])

print("First Three Elements:", arr[:3])
print("Last Three Elements:", arr[-3:])
print("Elements from Index 1 to 3:", arr[1:4])


# ---------------------------------------------------------
# 3. MATHEMATICAL OPERATIONS
# ---------------------------------------------------------

print("\n3. MATHEMATICAL OPERATIONS")

numbers = np.array([10, 20, 30, 40, 50])

print("Original:", numbers)
print("Addition:", numbers + 5)
print("Subtraction:", numbers - 5)
print("Multiplication:", numbers * 2)
print("Division:", numbers / 2)
print("Square:", numbers ** 2)
print("Square Root:", np.sqrt(numbers))


# ---------------------------------------------------------
# 4. AXIS-WISE OPERATIONS
# ---------------------------------------------------------

print("\n4. AXIS-WISE OPERATIONS")

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("2D Dataset:")
print(data)

print("Sum of all elements:", np.sum(data))

# axis=0 → column-wise
print("Column-wise Sum:", np.sum(data, axis=0))

# axis=1 → row-wise
print("Row-wise Sum:", np.sum(data, axis=1))

print("Column-wise Mean:", np.mean(data, axis=0))
print("Row-wise Mean:", np.mean(data, axis=1))


# ---------------------------------------------------------
# 5. STATISTICAL OPERATIONS
# ---------------------------------------------------------

print("\n5. STATISTICAL OPERATIONS")

dataset = np.array([10, 20, 30, 40, 50, 60, 70])

print("Dataset:", dataset)

print("Mean:", np.mean(dataset))
print("Median:", np.median(dataset))
print("Standard Deviation:", np.std(dataset))
print("Minimum:", np.min(dataset))
print("Maximum:", np.max(dataset))
print("Total:", np.sum(dataset))


# ---------------------------------------------------------
# 6. RESHAPING
# ---------------------------------------------------------

print("\n6. RESHAPING")

original = np.arange(1, 13)

print("Original Array:")
print(original)

reshaped = original.reshape(3, 4)

print("Reshaped Array (3 x 4):")
print(reshaped)

print("Shape:", reshaped.shape)


# ---------------------------------------------------------
# 7. BROADCASTING
# ---------------------------------------------------------

print("\n7. BROADCASTING")

marks = np.array([
    [50, 60, 70],
    [60, 70, 80],
    [70, 80, 90]
])

bonus = 5

print("Original Marks:")
print(marks)

print("After Adding 5 Bonus Marks:")
print(marks + bonus)


# ---------------------------------------------------------
# 8. SAVE AND LOAD NUMPY ARRAY
# ---------------------------------------------------------

print("\n8. SAVE AND LOAD NUMPY ARRAY")

save_array = np.array([100, 200, 300, 400, 500])

# Save array
np.save("my_array.npy", save_array)

print("Array saved successfully as 'my_array.npy'")

# Load array
loaded_array = np.load("my_array.npy")

print("Loaded Array:", loaded_array)


# ---------------------------------------------------------
# 9. PERFORMANCE COMPARISON
# Python List vs NumPy Array
# ---------------------------------------------------------

print("\n9. PERFORMANCE COMPARISON")

size = 1_000_000

# Python List
python_list = list(range(size))

start = time.time()

python_result = [x * 2 for x in python_list]

python_time = time.time() - start


# NumPy Array
numpy_array = np.arange(size)

start = time.time()

numpy_result = numpy_array * 2

numpy_time = time.time() - start


print("Python List Time:", python_time, "seconds")
print("NumPy Array Time:", numpy_time, "seconds")

if numpy_time < python_time:
    print("NumPy is faster for this operation.")
else:
    print("Python List was faster for this operation.")


# ---------------------------------------------------------
# PROJECT COMPLETED
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("        NUMPY DATA EXPLORER COMPLETED")
print("=" * 60)