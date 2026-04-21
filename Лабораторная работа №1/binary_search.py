# Бинарный поиск

# Реализация
def binary_search(array, element):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == element:
            return mid # будем просто возвращать индекс найденного элемента
        elif guess > element:
            high = mid - 1
        else:
            low = mid + 1
    return None


#a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(binary_search(a, 3))


# Функция измерения времени
import time

def measure_time(func, data1, data2):
    start = time.perf_counter()
    func(data1, data2)
    end = time.perf_counter()
    duration = end - start
    return f"{duration:.10f}" # выведет 10 знаков после запятой (как обычное число)


#print(measure_time(binary_search, a, 5))


# Функция генерации данных
import random

def generate_sorted_array(n):
    arr = []
    current = random.randint(0, 10)

    for _ in range(n):
        current += random.randint(1, 10) # всегда растём
        arr.append(current)

    return arr


#print(generate_sorted_array(1000))


# Эксперимент
if __name__ == '__main__':
    sizes = [100, 1000, 5000, 10000]
    search_value = 5
    for n in sizes:
        arr = generate_sorted_array(n)
        t = measure_time(binary_search, arr, search_value)
        print(n, t)