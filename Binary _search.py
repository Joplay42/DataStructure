import time

my_list = [1,6,7,9,10,11,17,23,28,31,33,38,39,45,48,50]

def linear_search(arr, value):
    start = time.perf_counter()
    for i in arr:
        if i == value:
            break

    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    print(f"Time: {elapsed_ms:.6f} ms")
    
def binary_search(arr, value): 
    start = time.perf_counter()
    
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == value:
            break

        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
               
    
    
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    print(f"Time: {elapsed_ms:.6f} ms")

linear_search(my_list, 50)
binary_search(my_list, 50)