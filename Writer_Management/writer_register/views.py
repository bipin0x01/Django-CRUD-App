from django.shortcuts import render
from .forms import WritersForm

# Create your views here.

def writers_list(request):
    return render(request,"writer_register/writers_list.html")

def writers_form(request):
    form = WritersForm()
    return render(request,"writer_register/writers_form.html")

def writers_delete(request):
    return