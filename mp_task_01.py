import threading
import time
import multiprocessing
import math
import requests

# список url для АТ-01
urls = ['https://www.example.com'] * 77


def fetch_url(url):
    response = requests.get(url)
    return response.text


def sequence():
    # время старта start_time
    start_time = time.perf_counter()
    # выполнение функции fetch_url для каждого url из urls
    for url in urls:
        fetch_url(url)
    # время окончания end_time
    end_time = time.perf_counter()
    print(f'sequence time: {end_time - start_time: 0.2f} \n')


def threads():
    # время старта start_time
    start_time = time.perf_counter()
    # выполнение с помощью потоков функции fetch_url для каждого url из urls (с ожиданием окончания выполнения всех потоков)
    threads: list[threading.Thread] = list()
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    # время окончания end_time
    end_time = time.perf_counter()
    print(f'threads time: {end_time - start_time: 0.2f} \n')


def processes():
    # время старта start_time
    start_time = time.perf_counter()
    # выполнение с помощью процессов функции fetch_url для каждого url из urls (с ожиданием окончания выполнения всех потоков)
    processes: list[multiprocessing.Process] = list()
    for url in urls:
        process = multiprocessing.Process(target=fetch_url, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    # время окончания end_time
    end_time = time.perf_counter()
    print(f'processes time: {end_time - start_time: 0.2f} \n')


if __name__ == '__main__':
    sequence()
    threads()
    processes()
    """
        Результатом должно стать (знаки вопроса заменятся на ваше время выполнения):
        
        sequence time:  ???

        threads time:  ???
        
        processes time:  ???
    """
