from django.db import models

CONVERT_CHOICES = (
    ("pdf", "PDF"),
    ("docx", "DOCX"),
    ("html", "HTML"),
)

class UserFileUpload(models.Model):
   current_choices = models.CharField(max_length = 20,choices = CONVERT_CHOICES)
   file = models.FileField() 
   convert_choices = models.CharField(max_length = 20,choices = CONVERT_CHOICES)