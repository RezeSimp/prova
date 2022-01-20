from os import name
from django.urls import path
from prova_pratica1.views import view_b,view_c,view_d
app_name="prova_pratica1"
urlpatterns=[
    path('view_b', view_b, name='view_b'),
    path('view_c', view_c, name='view_c'),
    path('view_d', view_d, name="view_d"),
]