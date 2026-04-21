# Проверка наличия элемента в массиве

# Реализация
def is_elem_in_array(array, element):
    for i in range(0, len(array)):
        if element == array[i]:
            return True
    return False


#a = [1, 2, 3, "mango", 5, 67, 8]
#print(is_elem_in_array(a, "mango"))


# Функция измерения времени
import time

def measure_time(func, data1, data2):
    start = time.perf_counter()
    func(data1, data2)
    end = time.perf_counter()
    duration = end - start
    return f"{duration:.10f}" # выведет 10 знаков после запятой (как обычное число)


#print(measure_time(is_elem_in_array, a, 5))


# Функция генерации данных
import random

def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr


#print(generate_array(5))


# Эксперимент
if __name__ == '__main__':
    sizes = [100, 1000, 5000, 10000]
    search_value = 5
    for n in sizes:
        arr = generate_array(n)
        t = measure_time(is_elem_in_array, arr, search_value)
        print(n, t)