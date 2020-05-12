from s1 import myfun1,c
from celery.result import AsyncResult
import datetime
#第一种方法
# s=myfun1.apply_async((10,20),countdown=5)
# print(s)
#延时 是生产者立即生产，消费者延时消费
#utc时间 国际时间 0时区的时间 格林威治时间
#utc --> 北京时间 +8小时
#北京 --> utc  -8小时
s=myfun1.apply_async((10,20),eta="utc时间")
print(s)

# 重试




