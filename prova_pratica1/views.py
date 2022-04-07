from urllib import response
from django.http import JsonResponse
from .models import Materia,Studente,Voti
from http.client import HTTPResponse
from multiprocessing import context
from re import template
from urllib import response
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

def view_API(request):
    materie= Materia.objects.all()
    data= {"materie": list(materie.values("pk","materia"))}
    response=JsonResponse(data)
    return response




# Create your views here.
def view_b(request):
     materie={
         'materia1':"Matematica",
         'materia2':"Italiano",
         'materia3':"Inglese",
         'materia4':"Storia",
         'materia5':"Geografia"
     }
     return render(request,"view_b.html",materie)
def view_c(request):
     context = {
         'GiuseppeGullo':[["Matematica",9,0],("Italiano",7,3),("Inglese",7.5,4),("Storia",7.5,4),("Geografia",5,7)],
         'AntonioBarbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9.5,0),("Storia",8,2),("Geografia",8,1)],
         'NicolaSpina':[("Matematica",7.5,2),("Italiano",6,2),("Inglese",4,3),("Storia",8.5,2),("Geografia",8,2)]
     }
     return render(request,"view_c.html",context)
class view_dView(ListView):
     model=Materia
     template_name="view_d.html"

     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context["materie"] = Materia.objects.all()
         return context

class view_eView(ListView):
     model=Studente
     template_name="view_e.html"
     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context["studenti"] = Studente.objects.all()
         return context

class VotoDetailView(DetailView):
     model=Voti
     template_name="voti_detail.html"

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["voti"] = Voti.objects.all()
        return context