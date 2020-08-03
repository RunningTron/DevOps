import time

from celery.result import AsyncResult

from celery_task.celery import task
from celery_task.e_mail import  e_mail_task
from celery_task.wechat import  wechat_task

t1 = e_mail_task.delay("163.com")
t2 = wechat_task.delay("微信")

print(t1.id,type(t1),type(t1.id))
print(t2.id,type(t1),type(t2.id))


task_id_dic = {t1.id:False,t2.id:False}
while 1:
    for task_id in task_id_dic:
        async_result = AsyncResult(id=task_id, app=task)
        if async_result.successful():
            if task_id_dic[task_id]:continue
            result = async_result.get()
            print(task_id,result)
            task_id_dic[task_id]=True
            # result.forget() # 将结果删除,执行完成，结果不会自动删除
            # async.revoke(terminate=True)  # 无论现在是什么时候，都要终止
            # async.revoke(terminate=False) # 如果任务还没有开始执行呢，那么就可以终止。
        elif async_result.failed():
            print('执行失败')
            # 只获取报错信息
            print(async_result.get(propagate=False))
            # 可以获取到源文件的报错位置
            print(async_result.traceback)
        elif async_result.status == 'PENDING':
            print('任务等待中被执行')
        elif async_result.status == 'RETRY':
            print('任务异常后正在重试')
        elif async_result.status == 'STARTED':
            print('任务已经开始被执行')



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