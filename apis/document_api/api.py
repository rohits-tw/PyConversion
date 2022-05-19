from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
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
from rest_framework import generics
from rest_framework.exceptions import ParseError
from rest_framework.parsers import MultiPartParser,FormParser

class DocumentConvertView(generics.GenericAPIView):
    parser_classes = (FormParser, MultiPartParser)
    serializer_class = DocumentConvertSerializers
    
    def post(self, request):
        serializer = DocumentConvertSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        

class DocumentConvertGetData(APIView):
    def get(self, request, id=None):
        if id:
            item = UserFileUpload.objects.get(id=id)
            if str(item.document_choices) == "pdftodocs":
                pdf_file = str(item.file.path)
                word_file = "test.docx"
                parse(pdf_file, word_file, start=0, end=None)
          
            elif str(item.document_choices) == "docxtohtml":
                docx_file = str(item.file.path)
                doc = aw.Document(docx_file)
                saveOptions = aw.saving.HtmlSaveOptions()
                saveOptions.export_roundtrip_information = True
                doc.save("Document.html", saveOptions)
                
            elif str(item.document_choices) == "htmltodoc":
                html_file = str(item.file.path)
                new_parser = HtmlToDocx()
                new_parser.parse_html_file(html_file, "index.docx")
          
            elif str(item.document_choices) == "pdftohtml":
                pdf_file = str(item.file.path)
                doc = aw.Document(pdf_file)
                doc.save("Output.html")
           
            else:
                html_file = str(item.file.path)
                pdfkit.from_file(html_file, 'out.pdf')
            return Response({"status": "success"}, status=status.HTTP_200_OK)

        items = UserFileUpload.objects.all()
        serializer = DocumentConvertSerializers(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    



