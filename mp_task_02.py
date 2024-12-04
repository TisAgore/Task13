import threading
import time
import multiprocessing
import math

# Функции для АТ-01

# запускать с n = 700008
def fibonacci(n):  # содержимое функции не менять
    """Возвращает последнюю цифру n-е числа Фибоначчи."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(f'fibonacci = {b % 10}')


# запускать с f, a, b, n равными соответственно math.sin, 0, math.pi, 20000000
def trapezoidal_rule(f, a, b, n):  # содержимое функции не менять
    """Вычисляет определенный интеграл функции f от a до b методом трапеций с n шагами."""
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        integral += f(a + i * h)
    print(f'trapezoidal_rule = {integral * h}')


def sequence():
    # время старта start_time
    start_time = time.perf_counter()
    # вычисление fibonacci от значения 700008
    fibonacci(700008)
    # вычисление trapezoidal_rule со значениями math.sin, 0, math.pi, 20000000
    trapezoidal_rule(math.sin, 0, math.pi, 20000000)
    # время окончания end_time
    end_time = time.perf_counter()
    print(f'sequence time: {end_time - start_time: 0.2f} \n')


def threads():
    # время старта start_time
    start_time = time.perf_counter()
    # вычисления на потоках:
    # 1. вычисление fibonacci от значения 700008
    thread1 = threading.Thread(target=fibonacci, args=(700008,))
    thread1.start()
    # 2. вычисление trapezoidal_rule со значениями math.sin, 0, math.pi, 20000000
    thread2 = threading.Thread(target=trapezoidal_rule, args=(math.sin, 0, math.pi, 20000000))
    thread2.start()
    
    thread1.join()
    thread2.join()
    # время окончания end_time
    end_time = time.perf_counter()
    print(f'threads time: {end_time - start_time: 0.2f} \n')


def processes():
    # время старта start_time
    start_time = time.perf_counter()
    # вычисления на процессах:
    # 1. вычисление fibonacci от значения 700008
    process1 = multiprocessing.Process(target=fibonacci, args=(700008,))
    process1.start()
    # 2. вычисление trapezoidal_rule со значениями math.sin, 0, math.pi, 20000000
    process2 = multiprocessing.Process(target=trapezoidal_rule, args=(math.sin, 0, math.pi, 20000000))
    process2.start()
    
    process1.join()
    process2.join()
    # время окончания end_time
    end_time = time.perf_counter()
    print(f'processes time: {end_time - start_time: 0.2f} \n')


if __name__ == '__main__':
    sequence()
    threads()
    processes()
    """
        Результатом должно стать (знаки вопроса заменятся на ваше время выполнения):
        
        fibonacci = 6
        trapezoidal_rule = 2.000000000000087
        sequence time:  ???
        
        fibonacci = 6
        trapezoidal_rule = 2.000000000000087
        threads time:  ??? 
        
        fibonacci = 6
        trapezoidal_rule = 2.000000000000087
        processes time:  ???
    """
