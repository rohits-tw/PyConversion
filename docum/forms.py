from django import forms
from .models import UserFileUpload

class UploadFileFormUser(forms.ModelForm):   
   class Meta:
      model = UserFileUpload
      fields = '__all__'