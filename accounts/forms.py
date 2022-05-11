from django import forms  
from .models import UserContactDetails

class UserContactRegistration(forms.ModelForm):
  class Meta:
    model = UserContactDetails
    fields = '__all__'