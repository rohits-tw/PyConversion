# Convert PDF file To Document File Code
from pdf2docx import parse
import aspose.words as aw
from htmldocx import HtmlToDocx
import pdfkit
import os 

def DocumentConvertCeleryTask(form_current_choices,form_file_data,form_convert_choices):
            if str(form_current_choices) == "pdf":
                if str(form_convert_choices) == "docx":
                    pdf_file = str(form_file_data)
                    word_file = "test.docx"
                    parse(pdf_file, word_file, start=0, end=None)
                        
            # End Code PDF file To Document File 
            
            # Convert Document To HTML File Code 
            
            elif str(form_current_choices) == "docx":
                if str(form_convert_choices) == "html":
                    docx_file = str(form_file_data)
                    doc = aw.Document(docx_file)
                    saveOptions = aw.saving.HtmlSaveOptions()
                    saveOptions.export_roundtrip_information = True
                    doc.save("Document.html", saveOptions)
                
            # End Code Convert Document to HTML file 
            
            # Convert HTML to Doxc File Code
            
            elif str(form_current_choices) == "html":
                if str(form_convert_choices) == "docx":
                    html_file = str(form_file_data)
                    new_parser = HtmlToDocx()
                    new_parser.parse_html_file(html_file, "index.docx")
                
            # End Code Convert HTML to Document file 
            
            # Convert PDF to HTML  Code
            
            elif str(form_current_choices) == "pdf":
                if str(form_convert_choices) == "html":
                    pdf_file = str(form_file_data)
                    doc = aw.Document(pdf_file)
                    doc.save("Output.html")
                
            # End Code Convert PDF to HTML file
            else:
                if str(form_current_choices) == "html":
                    if str(form_convert_choices) == "pdf":
                        html_file = str(form_file_data) 
                        pdfkit.from_file(html_file, 'out.pdf')