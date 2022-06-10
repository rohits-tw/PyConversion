from django.db import models

class UserContactDetails(models.Model):
  first_name = models.CharField(max_length = 100)
  last_name = models.CharField(max_length = 100)
  user_email = models.EmailField()
  contact_number = models.CharField(max_length = 10)
  
  def __str__(self):
    return self.first_name
