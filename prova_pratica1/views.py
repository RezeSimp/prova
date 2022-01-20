from multiprocessing import context
from django.shortcuts import render

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