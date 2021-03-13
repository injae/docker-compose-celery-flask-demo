from os import environ
from celery import Celery

broker_url = environ['BROKER_URL']
result_backend = environ['RESULT_BACKEND']

app = Celery('tasks', backend=result_backend, broker=broker_url)

@app.task
def add(x,y):
    return x + y
