# Бинарный поиск

# Реализация
def multiplication_table(n):
    lines = []
    
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(str(i * j))
        lines.append(" ".join(row))
    
    return "\n".join(lines)


#print(multiplication_table(3))


# Функция измерения времени
import time

def measure_time(func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    duration = end - start
    return f"{duration:.10f}" # выведет 10 знаков после запятой (как обычное число)


#print(measure_time(multiplication_table, 5))


# Функция генерации данных - по сути она нам не нужна в эксперименте, так как мы будем просто работать с числом
import random

def generate_n():
    return random.randint(0, 10000)


#print(generate_n())


# Эксперимент
if __name__ == '__main__':
    sizes = [100, 1000, 5000, 10000]
    for n in sizes:
        t = measure_time(multiplication_table, n)
        print(n, t)