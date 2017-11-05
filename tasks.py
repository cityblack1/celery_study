from celery import Celery

app = Celery('tasks', broker='redis://:''@127.0.0.1:6379/2', backend='redis://:''@127.0.0.1:6379/3')


@app.task
def add(x, y):
    return x + y