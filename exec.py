import time

from celery.result import AsyncResult

from celery_task.celery import task
from celery_task.e_mail import  e_mail_task
from celery_task.wechat import  wechat_task

t1 = e_mail_task.delay("163.com")
t2 = wechat_task.delay("微信")
print(t1,type(t1))
print(t2,type(t2))
print(t1.id,type(t1.id))
print(t2.id,type(t2.id))

res = AsyncResult(id=t1.id,app=task)
print(res.status)
print(res.successful())
print(res.result)
print(res.get())

# 只获取报错信息
print(res.get(propagate=False))
#可以获取到源文件的报错位置
print(res.traceback)

'''
s=myfun1.delay()
# print(s,type(s))
# print(s.id,type(s.id))
# 夯住
res=AsyncResult(id=s.id,app=c)
#获取返回值
# print(res.status)
# print(res.successful())
# 只获取报错信息
print(res.get(propagate=False))
#可以获取到源文件的报错位置
print(res.traceback)
# print(res.status)
# print(res.successful())
'''