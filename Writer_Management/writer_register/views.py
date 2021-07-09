from django.shortcuts import redirect, render
from .forms import WritersForm
from .models import Writers
# Create your views here.

def writers_list(request):
    context = {'writers_list' : Writers.objects.all()}
    return render(request,"writer_register/writers_list.html",context)

def writers_form(request):
    form = WritersForm()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WritersForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return redirect('/writers/list/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = WritersForm()
    return render(request,"writer_register/writers_form.html",{'form':form})

def writers_delete(request):
    return