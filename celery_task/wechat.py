from celery_task.celery import task
import time
import random


@task.task
def wechat_task(addr):
    time.sleep(random.randint(5))
    print("send wechat to %s" % addr)
    return "wechat", addr
