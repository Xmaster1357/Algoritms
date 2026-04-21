# Замеры алгоритмической и пространственной сложности любой из сортировок
# Insertion Sort
# Реализация
def insertion_sort(arr):
    a = arr.copy()
    
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        
        a[j + 1] = key
    
    return a


# Замер времени (алгоритмическая сложность)
import time

def measure_time(func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    duration = end - start
    return f"{duration:.10f}"


# Замер пространственной сложности (в МБ)
import sys

def deep_size(arr):
    return sys.getsizeof(arr) + sum(sys.getsizeof(x) for x in arr)

def measure_memory(func, data):
    before = deep_size(data)
    result = func(data)
    after = deep_size(result)
    
    # разница + перевод в МБ
    diff = abs(after - before) / (1024 * 1024)

    return f"{diff:.6f} MB"


# Генерация данных
import random

def generate_array(n):
    return [random.randint(0, 10000) for _ in range(n)]


# Эксперимент
if __name__ == '__main__':
    sizes = [100, 1000, 5000, 10000]

    for n in sizes:
        arr = generate_array(n)
        
        t = measure_time(insertion_sort, arr)
        mem = measure_memory(insertion_sort, arr)
        
        print(n, t, mem)