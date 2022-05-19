from __future__ import absolute_import
from celery import shared_task
import django.contrib
from time import sleep
from .utils import DocumentConvertCeleryTask
from celery import  shared_task, Celery 
from time import sleep
from celery_progress.backend import ProgressRecorder
# app = Celery('task', backend='redis', broker='redis://localhost:6379')

@shared_task(bind=True)
def go_to_sleep(self, duration):
  progress_recorder = ProgressRecorder(self)
  result =0
  for i in range(100):
    sleep(duration)
    result +=1
    progress_recorder.set_progress(i + 1, duration)
    #sleep(duration)
    return result


@shared_task
def sleepy(duration):
  sleep(duration)
  return None

@shared_task
def document_converter_celery_task_function(form_current_choices,form_file_data,form_convert_choices):
  DocumentConvertCeleryTask(form_current_choices,form_file_data,form_convert_choices)
  return None