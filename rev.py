import time

from celery_task.celery import task
from celery_task.e_mail import e_mail_task
from _datetime import datetime
from celery.result import AsyncResult
from celery.schedules import crontab

crontab()
t1 = datetime(2020, 8, 3, 22, 20, 00)

task_time = datetime.utcfromtimestamp(t1.timestamp())



'''
ctime = datetime.now()
# 默认用utc时间
utc_ctime = datetime.utcfromtimestamp(ctime.timestamp())
from datetime import timedelta

time_delay = timedelta(seconds=10)
task_time = utc_ctime + time_delay
'''

ret = e_mail_task.apply_async(args=["163"], eta=task_time)
task_id = ret.id

async_result = AsyncResult(id=task_id, app=task)
while 1:
    if async_result.successful():
        result = async_result.get()
        print(result)
        break
        # result.forget() # 将结果删除,执行完成，结果不会自动删除
        # async.revoke(terminate=True)  # 无论现在是什么时候，都要终止
        # async.revoke(terminate=False) # 如果任务还没有开始执行呢，那么就可以终止。
    elif async_result.failed():
        print('执行失败')
    elif async_result.status == 'PENDING':
        print('任务等待中被执行')
    elif async_result.status == 'RETRY':
        print('任务异常后正在重试')
    elif async_result.status == 'STARTED':
        print('任务已经开始被执行')
    time.sleep(1)
