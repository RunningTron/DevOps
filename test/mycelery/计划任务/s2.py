from s1 import myfun1,c
from celery.beat import crontab
#周期任务
c.conf.beat_schedule={
    "5s":{
        "task":"s1.myfun1",
        "schedule":5,
        "args":(10,20)
    },
    "cron":{
        "task":"s1.myfun1",
        "schedule":crontab(minute=40),
        "args":(20,30)
    }
}




