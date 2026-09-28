"""Сортировки: реализация и бенчмарк."""
import time
import random

def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    arr = arr.copy()
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(l, r):
    res = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i]); i += 1
        else:
            res.append(r[j]); j += 1
    res.extend(l[i:]); res.extend(r[j:])
    return res

def benchmark():
    sizes = [100, 500, 1000]
    algorithms = {
        "bubble": bubble_sort,
        "insertion": insertion_sort,
        "selection": selection_sort,
        "quick": quick_sort,
        "merge": merge_sort,
    }
    for size in sizes:
        data = [random.randint(0, 10000) for _ in range(size)]
        print(f"\nРазмер: {size}")
        for name, algo in algorithms.items():
            start = time.time()
            result = algo(data)
            elapsed = time.time() - start
            assert result == sorted(data), f"{name} failed"
            print(f"  {name}: {elapsed:.4f}s")

if __name__ == "__main__":
    benchmark()
