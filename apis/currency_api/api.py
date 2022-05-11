from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CurrencyConvertSerializers
from apis.models import Currency_convert
from rest_framework.schemas import AutoSchema
import coreapi

class CurrencyConvertView(APIView):
    def post(self, request):
        serializer = CurrencyConvertSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CurrencyConvertGetData(APIView):
    def get(self, request, id=None):
        if id:
            item = Currency_convert.objects.get(id=id)
            if  str(item.current_choice) == "Indian Rupee":
                with open('api/api11.txt') as f:
                    lines = f.readlines()
                    currencyDict = {}
                    for line in lines:
                        parsed = line.split("\t")
                        currencyDict[parsed[0]] = parsed[1] 
                    if str(item.convert_choice) == "usd":
                        result = item.amount * float(currencyDict[item.convert_choice])
                    else:
                        result = item.amount * float(currencyDict[item.convert_choice])
            return Response({"status": "success", "current_choice" : item.current_choice,"amount" : item.amount,"convert_choice" : item.convert_choice,"Result":result}, status=status.HTTP_200_OK)

        items = Currency_convert.objects.all()
        serializer = CurrencyConvertSerializers(items, many=True)
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
    