from celery import Celery

app = Celery('add_tasks', broker='redis:''//127.0.0.1:6379/2', backend='redis:''//127.0.0.1:6379/3')
app.conf.update(
    # 配置所在的时区
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_ENABLE_UTC=True,
    # 官网推荐消息序列化方式为json
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    # 配置定时任务
    CELERYBEAT_SCHEDULE={
        'my_task': {
            'task': 'task2.add',  # tasks.py模块下的add方法
            'schedule': 60,  # 每隔60运行一次
            'args': (23, 12),
        }
    }

)


@app.task
def add(x, y):
    return x + y