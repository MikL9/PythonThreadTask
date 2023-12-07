import threading
import random
import multiprocessing

def multiply_array(array):
    for i in range(len(array)):
        array[i] *= random.uniform(-1500, 1500)

array = [random.randint(-1500, 1500) for _ in range(100000000)]

multiply_array(array)

def multiply_array_threaded(array, num_threads):
    threads = []
    chunk_size = len(array) // num_threads
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size
        threads.append(threading.Thread(target=multiply_array_chunk, args=(array[start:end],)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

def multiply_array_chunk(array_chunk):
    for i in range(len(array_chunk)):
        array_chunk[i] *= random.uniform(-1500, 1500)

array = [random.randint(-1500, 1500) for _ in range(100000000)]

multiply_array_threaded(array, 10)

def multiply_array_multiprocessed(array, num_processes):
    processes = []
    chunk_size = len(array) // num_processes
    for i in range(num_processes):
        start = i * chunk_size
        end = (i + 1) * chunk_size
        processes.append(multiprocessing.Process(target=multiply_array_chunk, args=(array[start:end],)))
    for process in processes:
        process.start()
    for process in processes:
        process.join()

multiply_array_multiprocessed(array, 10)

