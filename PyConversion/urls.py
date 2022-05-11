from django.contrib import admin
from django.urls import path , include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Currency Conversion API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('currency/',include('currency.urls')),
    path('documents/',include('docum.urls')),
    path('api/',include('apis.urls')),
    path('docs/', schema_view),
]
