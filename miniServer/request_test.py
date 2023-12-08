import requests
import time

data = {'data': 'example_data'}

print(f"Отправка задачи с данными: {data}")
response = requests.post('http://127.0.0.1:5000/submit_task', json=data)

if response.status_code == 202:
    task_id = response.json()['task_id']
    print(f"Задача успешно принята. Task ID: {task_id}")
    time.sleep(5)

    result_response = requests.get(f'http://127.0.0.1:5000/get_result/{task_id}')

    if result_response.status_code == 200:
        print(f"Задача выполнена успешно! Result: {result_response.json()}")
    else:
        print(f"Ошибка обработки. Status code: {result_response.status_code}, Response: {result_response.text}")
else:
    print(f"Задача не принята. Status code: {response.status_code}, Response: {response.text}")
