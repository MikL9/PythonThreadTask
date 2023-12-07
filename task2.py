import os
import concurrent.futures
import time

def count_hello_world_occurrences(content):
    return content.count("HelloWorld")

def process_files(folder_path):
    result = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                file_content = file.read()
                hello_world_count = count_hello_world_occurrences(file_content)
                result.append((filename, hello_world_count))

    return result

def process_file(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
        hello_world_count = count_hello_world_occurrences(file_content)
        return file_path, hello_world_count

def process_files_parallel(folder_path):
    files = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, filename))]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(process_file, files))

    return results

if __name__ == "__main__":
    folder_path = "randomFiles"

    # Измерение времени выполнения для последовательной обработки файлов
    start_time = time.time()
    results_sequential = process_files(folder_path)
    end_time = time.time()
    print(f"Sequential Execution Time: {end_time - start_time} seconds")

    # Измерение времени выполнения для многопоточной обработки файлов
    start_time = time.time()
    results_parallel = process_files_parallel(folder_path)
    end_time = time.time()
    print(f"Parallel Execution Time: {end_time - start_time} seconds")

    # Вывод результатов
    for filename, hello_world_count in results_sequential:
        print(f"Sequential - File: {filename}, HelloWorld Count: {hello_world_count}")

    # for filename, hello_world_count in results_parallel:
    #     print(f"Parallel - File: {filename}, HelloWorld Count: {hello_world_count}")