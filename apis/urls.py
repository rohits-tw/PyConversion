from django.urls import path
from apis.document_api.api import DocumentConvertView ,DocumentConvertGetData 
from apis.currency_api.api import CurrencyConvertView ,CurrencyConvertGetData

urlpatterns = [
    path('currencypostdata/', CurrencyConvertView.as_view()),
    path('currencygetdata/<int:id>/',CurrencyConvertGetData.as_view()),
    path('documentpostdata/', DocumentConvertView.as_view()),
    path('documentgetdata/<int:id>/',DocumentConvertGetData.as_view()),
]