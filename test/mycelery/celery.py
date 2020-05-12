from celery import Celery
c=Celery('task',broker='redis://alexdsb@10.0.0.129:6379/2',backend="redis://alexdsb@10.0.0.129:6379/3",
         include=["mycelery.s1","mycelery.s2"])
