from os import name
from django.urls import path
from prova_pratica1.views import view_b,view_c, view_API, view_dView, view_eView, VotoDetailView
app_name="prova_pratica1"
urlpatterns=[
    path('view_b', view_b, name='view_b'),
    path('view_c', view_c, name='view_c'),
    path("view_d", view_dView.as_view(), name="view_d"),
    path("view_e", view_eView.as_view(), name="view_e"),
    path("voti/<int:pk>", VotoDetailView.as_view(), name="voti_detail" ),
    path('materie/', view_API, name="view_API")

]