from django.shortcuts import render

# Create your views here.
def view_b(request):
    return render(request, "view_b.html"),
def view_c(request):
    return render(request, "view_c.html")