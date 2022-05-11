from django.db import models

CONVERT_CHOICES = (
    ("US Dollar", "USD"),
    ("Euro", "EURO"),
    ("British Pound","ASTRLN"),
    ("Australian Dollar","BRTSH"),
    ("Canadian Dollar", "CNDN"),
    ("Singapore Dollar", "SNGPR"),
    ("Swiss Franc", "SWSFRNC"),
    ("Malaysian Ringgit","MLYSN"),
    ("Japanese Yen","JPNS"),
    ("Chinese Yuan Renminbi","CHNS"),
    ("Indian Rupee","INR"),
) 


class Currency_convert(models.Model):
    current_choice = models.CharField(max_length = 50 , choices= CONVERT_CHOICES)
    amount = models.IntegerField()
    convert_choice = models.CharField(max_length = 50 , choices= CONVERT_CHOICES)
    result = models.IntegerField(null=True)
    
    


CONVERT_CHOICESES = (
    ("pdftodocs", "PDF TO DOCX"),
    ("docxtohtml", "DOCX TO HTML"),
    ("htmltodoc", "HTML TO DOCX"),
    ("pdftohtml", "PDF TO HTML"),
    ("htmltopdf", "HTML TO PDF"),
)


class UserFileUpload(models.Model):
   file = models.FileField() 
   document_choices = models.CharField(max_length = 20,choices = CONVERT_CHOICESES)