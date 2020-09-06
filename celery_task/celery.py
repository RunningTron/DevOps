# -*- encoding: utf-8 -*-
from __future__ import absolute_import  # 使用绝对导入
from celery import Celery

task = Celery("message",
              broker="redis://:123@47.96.232.142:6379/1",
              backend="redis://:123@47.96.232.142:6379/3",
              include=["celery_task.e_mail", "celery_task.wechat"])

# 时区
task.conf.timezone = 'Asia/Shanghai'
# 是否使用UTC
task.conf.enable_utc = False
