from django.urls import path
from prima_applicazione.views import homepage

app_name="prima_applicazione"
urlpatterns=[
    path('', homepage, name='homepage'),
]