from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DocumentConvertSerializers
from apis.models import UserFileUpload
from rest_framework.schemas import AutoSchema 
import coreapi
from pdf2docx import parse
import aspose.words as aw
from htmldocx import HtmlToDocx
import pdfkit
import os 


class DocumentConvertView(APIView): 
    def post(self, request):
        serializer = DocumentConvertSerializers(data=request.POST ,files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class DocumentConvertGetData(APIView):
    def get(self, request, id=None):
        if id:
            item = UserFileUpload.objects.get(id=id)
            print(item)
            if str(item.document_choices) == "pdftodocs":
                pdf_file = str(item.file)
                word_file = "test.docx"
                parse(pdf_file, word_file, start=0, end=None)
          
            elif str(item.document_choices) == "docxtohtml":
                docx_file = str(item.file)
                doc = aw.Document(docx_file)
                saveOptions = aw.saving.HtmlSaveOptions()
                saveOptions.export_roundtrip_information = True
                doc.save("Document.html", saveOptions)
                
            elif str(item.document_choices) == "htmltodoc":
                html_file = str(item.file)
                new_parser = HtmlToDocx()
                new_parser.parse_html_file(html_file, "index.docx")
          
            elif str(item.document_choices) == "pdftohtml":
                pdf_file = str(form_file_data)
                doc = aw.Document(pdf_file)
                doc.save("Output.html")
           
            else:
                html_file = str(item.file)
                pdfkit.from_file(html_file, 'out.pdf')
            return Response({"status": "success","data": serializer.item}, status=status.HTTP_200_OK)

        items = UserFileUpload.objects.all()
        serializer = DocumentConvertSerializers(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    





class CustomLoginSchema(AutoSchema):
    def get_serializer_fields(self, path, method):
        if method == 'POST':
            extra_fields = [
                coreapi.Field('username',required=True,location="formData",type="string"),
                coreapi.Field('password',required=True,location="formData",type="string"),
            ]
        else:
            extra_fields = []
        serializer_fields = super().get_serializer_fields(path, method)
        return serializer_fields + extra_fields
    