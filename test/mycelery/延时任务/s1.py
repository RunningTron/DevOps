from celery import Celery

# broker 可以是redis，可以是rabbitmq
# redis 库 0-15 总共16个
# c=Celery('task',broker='redis://10.0.0.129:6379/2')
#密码
# 获取任务时，是谁有时间谁就去申请
# 生产者不会管消费者执行成功与否
c=Celery('task',broker='redis://:alexdsb@10.0.0.129:6379/2',backend="redis://:alexdsb@10.0.0.129:6379/3")
import time
@c.task
def myfun1(a,b):
    # time.sleep(10)
    return f'myfun1{a}{b}'

@c.task
def myfun2():
    return 'myfun2'

@c.task
def myfun3():
    return 'myfun3'