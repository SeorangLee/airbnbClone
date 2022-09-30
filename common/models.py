from django.db import models

class CommonModel(models.Model):

  """Common Model Definition"""
  created_at = models.DateTimeField(auto_now_add=True)  #처음저장할때 시간
  updated_at = models.DateTimeField(auto_now=True)   #업데이트할때 시간

  class Meta: 
    abstract = True # DB에 해당 모델을 업데이트 하지 않음