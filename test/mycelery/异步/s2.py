from s1 import myfun1,c
from celery.result import AsyncResult

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




