
from celery import Celery

app = Celery('bear')
app.config_from_object('learn_celery.config')


@app.task(bind=True)
def add(x, y):
    return x + y



