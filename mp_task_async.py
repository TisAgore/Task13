import time
import math
import requests
import asyncio

async def fetch_url(url):
    response = requests.get(url)
    return response.text

# запускать с n = 700008
async def fibonacci(n):
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
async def trapezoidal_rule(f, a, b, n):
    """Вычисляет определенный интеграл функции f от a до b методом трапеций с n шагами."""
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        integral += f(a + i * h)
    print(f'trapezoidal_rule = {integral * h}')


async def task1():
    urls = ['https://www.example.com'] * 77
    tasks = list()
    start_time = time.perf_counter()
    for url in urls:
        task = asyncio.create_task(fetch_url(url))
        tasks.append(task)

    for task in tasks:
        await task
    end_time = time.perf_counter()
    print(f'task1 time: {end_time - start_time: 0.2f} \n')

async def task2():
    start_time = time.perf_counter()
    task_fib = asyncio.create_task(fibonacci(700008))
    task_trap = asyncio.create_task(trapezoidal_rule(math.sin, 0, math.pi, 20000000))

    await task_fib
    await task_trap
    end_time = time.perf_counter()
    print(f'task2 time: {end_time - start_time: 0.2f} \n')

asyncio.run(task1())
asyncio.run(task2())