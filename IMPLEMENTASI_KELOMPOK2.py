import time
import matplotlib.pyplot as plt
import random

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1

sizes = [1, 10, 20, 30, 40, 50, 100, 500, 1000, 5000, 10000]
binary_search_times = []
sequential_search_times = []

for size in sizes:
    data = list(range(size))
    target = random.randint(0, size - 1)

    # Measure time for Binary Search
    start_time = time.time()
    binary_search(data, target)
    end_time = time.time()
    binary_search_times.append(end_time - start_time)

    # Measure time for Sequential Search
    start_time = time.time()
    sequential_search(data, target)
    end_time = time.time()
    sequential_search_times.append(end_time - start_time)
    
# #output angka
# print(sequential_search(data, 100000))
# print(binary_search(data, 100000))


# Plotting
plt.plot(sizes, binary_search_times, label='Binary Search')
plt.plot(sizes, sequential_search_times, label='Sequential Search')
plt.xlabel('Input Size')
plt.ylabel('Running Time')
plt.legend()
plt.show()
