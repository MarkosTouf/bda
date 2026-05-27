import multiprocessing as mp
import random
import time

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


def generate_and_sort_numbers(n=10000):
    numbers = [random.random() for _ in range(n)]
    bubble_sort(numbers)

def serial_runner(runs=3):
    start = time.perf_counter()

    # TODO: call generate_and_sort_numbers() runs times

    generate_and_sort_numbers(runs)

    end = time.perf_counter()
    return end - start

def parallel_runner(runs=3):
    start = time.perf_counter()

    processes = []

    # TODO: create runs processes
    p1 = mp.Process(target=generate_and_sort_numbers, args = (10000,))
    p2 = mp.Process(target=generate_and_sort_numbers, args = (10000,))
    p3 = mp.Process(target=generate_and_sort_numbers, args = (10000,))
    # TODO: start each process    
    p1.start()
    p2.start()
    p3.start()
    # TODO: wait for each process to finish
    p1.join()
    p2.join()
    p3.join()

    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    serial_time = serial_runner(runs=100)
    parallel_time = parallel_runner(runs=3)

    print(f"Serial time: {serial_time:.2f}s")
    print(f"Parallel time: {parallel_time:.2f}s")