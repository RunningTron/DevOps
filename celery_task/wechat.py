from celery_task.celery import task
import time
import random


@task.task
def wechat_task(addr):
    time.sleep(random.randint(1,3))
    print("send wechat to %s" % addr)
    return "wechat", addr
