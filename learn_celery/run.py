from learn_celery.celery import add
import time


def test():
    time.sleep(5)
    add.delay(2, 3)







































