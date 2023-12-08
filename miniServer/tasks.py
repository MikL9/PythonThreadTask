from celery import Celery
import time

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def process_data(data):
    print(f"Processing data: {data}")
    time.sleep(5)  # Имитация
    print(f"Data processed: {data}")
    return f"Processed data: {data}"
