from django.db import models

CONVERT_CHOICES = (
    ("pdftodocs", "PDF TO DOCX"),
    ("docxtohtml", "DOCX TO HTML"),
    ("htmltodoc", "HTML TO DOCX"),
    ("pdftohtml", "PDF TO HTML"),
    ("htmltopdf", "HTML TO PDF"),
)


class UserFileUpload(models.Model):
   file = models.FileField() 
   document_choices = models.CharField(max_length = 20,choices = CONVERT_CHOICES)