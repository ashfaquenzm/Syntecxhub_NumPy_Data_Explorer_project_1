import streamlit as st
import numpy as np
import time

st.set_page_config(page_title="NumPy Data Explorer", layout="wide")

st.title("📊 NumPy Data Explorer")
st.markdown("---")

# ---------------------------------------------------------
# 1. ARRAY CREATION
# ---------------------------------------------------------
st.header("1. Array Creation")
col1, col2 = st.columns(2)

with col1:
    arr = np.array([10, 20, 30, 40, 50])
    st.write("**Basic Array:**", arr)
    
    zeros = np.zeros(5)
    st.write("**Zeros Array:**", zeros)

with col2:
    ones = np.ones(5)
    st.write("**Ones Array:**", ones)
    
    range_array = np.arange(1, 11)
    st.write("**Range Array (1 to 10):**", range_array)

st.markdown("---")

# ---------------------------------------------------------
# 2. INDEXING AND SLICING
# ---------------------------------------------------------
st.header("2. Indexing and Slicing")
st.write("**Original Array:**", arr)

col1, col2 = st.columns(2)
with col1:
    st.write(f"First Element: `{arr[0]}`")
    st.write(f"Third Element: `{arr[2]}`")
    st.write(f"Last Element: `{arr[-1]}`")

with col2:
    st.write(f"First Three Elements: `{arr[:3]}`")
    st.write(f"Last Three Elements: `{arr[-3:]}`")
    st.write(f"Elements from Index 1 to 3: `{arr[1:4]}`")

st.markdown("---")

# ---------------------------------------------------------
# 3. MATHEMATICAL OPERATIONS
# ---------------------------------------------------------
st.header("3. Mathematical Operations")
numbers = np.array([10, 20, 30, 40, 50])
st.write("**Original:**", numbers)

col1, col2, col3 = st.columns(3)
with col1:
    st.write("**Addition (+5):**", numbers + 5)
    st.write("**Subtraction (-5):**", numbers - 5)
with col2:
    st.write("**Multiplication (*2):**", numbers * 2)
    st.write("**Division (/2):**", numbers / 2)
with col3:
    st.write("**Square (^2):**", numbers ** 2)
    st.write("**Square Root:**", np.sqrt(numbers))

st.markdown("---")

# ---------------------------------------------------------
# 4. AXIS-WISE OPERATIONS
# ---------------------------------------------------------
st.header("4. Axis-wise Operations")
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

st.write("**2D Dataset:**")
st.dataframe(data)

st.write(f"**Sum of all elements:** `{np.sum(data)}`")
st.write(f"**Column-wise Sum (axis=0):** `{np.sum(data, axis=0)}`")
st.write(f"**Row-wise Sum (axis=1):** `{np.sum(data, axis=1)}`")
st.write(f"**Column-wise Mean:** `{np.mean(data, axis=0)}`")
st.write(f"**Row-wise Mean:** `{np.mean(data, axis=1)}`")

st.markdown("---")

# ---------------------------------------------------------
# 5. STATISTICAL OPERATIONS
# ---------------------------------------------------------
st.header("5. Statistical Operations")
dataset = np.array([10, 20, 30, 40, 50, 60, 70])
st.write("**Dataset:**", dataset)

st.json({
    "Mean": float(np.mean(dataset)),
    "Median": float(np.median(dataset)),
    "Standard Deviation": float(np.std(dataset)),
    "Minimum": int(np.min(dataset)),
    "Maximum": int(np.max(dataset)),
    "Total Sum": int(np.sum(dataset))
})

st.markdown("---")

# ---------------------------------------------------------
# 6. RESHAPING
# ---------------------------------------------------------
st.header("6. Reshaping")
original = np.arange(1, 13)
st.write("**Original Array (1D):**", original)

reshaped = original.reshape(3, 4)
st.write("**Reshaped Array (3 x 4):**")
st.dataframe(reshaped)

st.markdown("---")

# ---------------------------------------------------------
# 7. BROADCASTING
# ---------------------------------------------------------
st.header("7. Broadcasting")
marks = np.array([
    [50, 60, 70],
    [60, 70, 80],
    [70, 80, 90]
])
bonus = 5

st.write("**Original Marks:**")
st.dataframe(marks)

st.write("**After Adding 5 Bonus Marks:**")
st.dataframe(marks + bonus)

st.markdown("---")

# ---------------------------------------------------------
# 8. SAVE AND LOAD NUMPY ARRAY
# ---------------------------------------------------------
st.header("8. Save and Load NumPy Array")
save_array = np.array([100, 200, 300, 400, 500])
np.save("my_array.npy", save_array)
st.success("Array successfully saved as `my_array.npy`!")

loaded_array = np.load("my_array.npy")
st.write("**Loaded Array:**", loaded_array)

st.markdown("---")

# ---------------------------------------------------------
# 9. PERFORMANCE COMPARISON
# ---------------------------------------------------------
st.header("9. Performance Comparison (List vs NumPy)")

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

st.write(f"⏱️ **Python List Time:** `{python_time:.6f}` seconds")
st.write(f"⚡ **NumPy Array Time:** `{numpy_time:.6f}` seconds")

if numpy_time < python_time:
    speedup = python_time / numpy_time
    st.info(f"NumPy is approx **{speedup:.2f}x faster** than Python List!")
else:
    st.info("Python List was faster for this operation.")
