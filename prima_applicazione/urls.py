from os import name
from django.urls import path
from prima_applicazione.views import homepage,welcome,lista

app_name="prima_applicazione"
urlpatterns=[
    path('', homepage, name='homepage'),
    path('welcome', welcome, name="welcome.html"),
    path('lista', lista, name="lista"),
]