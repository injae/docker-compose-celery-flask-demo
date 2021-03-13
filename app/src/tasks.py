from celery import Celery

celery_app = Celery('tasks', backend='rpc://', broker='pyamqp://rabbitmq:5672')
