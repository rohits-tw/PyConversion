from django.shortcuts import render ,redirect
from django.http import HttpResponseRedirect
from .forms import UploadFileFormUser
from .models import UserFileUpload
from pdf2docx import parse
import aspose.words as aw
from htmldocx import HtmlToDocx
import pdfkit
import os 

# Document Conversion Code Start
 
def docx2pdf_converter(request):
    if request.method == 'POST':
        form = UploadFileFormUser(request.POST, request.FILES)
        if form.is_valid():
            form_file_data = form.cleaned_data['file']
            form_choice_data = form.cleaned_data['document_choices']
            
            # Convert PDF file To Document File Code
            
            if str(form_choice_data) == "pdftodocs":
                pdf_file = str(form_file_data)
                word_file = "test.docx"
                parse(pdf_file, word_file, start=0, end=None)
                    
            # End Code PDF file To Document File 
            
            # Convert Document To HTML File Code 
            
            elif str(form_choice_data) == "docxtohtml":
                docx_file = str(form_file_data)
                doc = aw.Document(docx_file)
                saveOptions = aw.saving.HtmlSaveOptions()
                saveOptions.export_roundtrip_information = True
                doc.save("Document.html", saveOptions)
                
            # End Code Convert Document to HTML file 
            
            # Convert HTML to Doxc File Code
            
            elif str(form_choice_data) == "htmltodoc":
                html_file = str(form_file_data)
                new_parser = HtmlToDocx()
                new_parser.parse_html_file(html_file, "index.docx")
                
            # End Code Convert HTML to Document file 
            
            # Convert PDF to HTML  Code
            
            elif str(form_choice_data) == "pdftohtml":
                pdf_file = str(form_file_data)
                doc = aw.Document(pdf_file)
                doc.save("Output.html")
                
            # End Code Convert PDF to HTML file
            else:
                html_file = str(form_file_data)
                pdfkit.from_file(html_file, 'out.pdf')

    else:
        form = UploadFileFormUser()
    return render(request, 'docversion.html', {'form': form})

# End Document Conversion Code