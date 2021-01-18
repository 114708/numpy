import time
import random
import numpy as np

limit = 1000000
nums = []

start = time.perf_counter()

for _ in range(limit):
    nums.append(random.randint(0, limit))

min = limit + 1
for num in nums:
    if num < min:
        min = num
end = time.perf_counter()
elapsed = end - start
print(f"Elapsed ti,e for python is {elapsed}")

###
#now do the same using numpy
###
start = time.perf_counter()

nums = np.random.randint(0, limit, limit)
min = nums.min()

end = time.perf_counter()
elapsed_numpy = end - start
print(f"Elapsed time for numpy is {elapsed_numpy}")
