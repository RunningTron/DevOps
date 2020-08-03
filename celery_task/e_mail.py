from celery_task.celery import task
import time
import random

@task.task
def e_mail_task(addr):
    time.sleep(random.randint(5,8))
    print("send e_mail to %s"%addr)
    return "e_mail",addr