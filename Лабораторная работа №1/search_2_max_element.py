# Поиск второго максимального элемента

# Реализация
def second_max_in_array(array):
    max1 = array[0]
    max2 = array[0]
    for i in range(0, len(array)):
        if array[i] > max1:
            max2 = max1
            max1 = array[i]
        elif array[i] > max2 and array[i] != max1:
            max2 = array[i]
    return max2


#a = [5, 122, 32, 778, 1024, 11]
#print(second_max_in_array(a))


# Функция измерения времени
import time

def measure_time(func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    duration = end - start
    return f"{duration:.10f}" # выведет 10 знаков после запятой (как обычное число)


#print(measure_time(second_max_in_array, a))


# Функция генерации данных
import random

def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr


#print(generate_array(7))


# Эксперимент
if __name__ == '__main__':
    sizes = [100, 1000, 5000, 10000]
    for n in sizes:
        arr = generate_array(n)
        t = measure_time(second_max_in_array, arr)
        print(n, t)