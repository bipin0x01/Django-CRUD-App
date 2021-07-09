from django.shortcuts import redirect, render
from .forms import WritersForm
from .models import Writers
# Create your views here.

def writers_list(request):
    context = {'writers_list' : Writers.objects.all()}
    return render(request,"writer_register/writers_list.html",context)

def writers_form(request,id=0):
    form = WritersForm()
    if request.method == 'POST':
        if id==0:     #If Insert operation
            form = WritersForm(request.POST)   # create a form instance and populate it with data from the request:
        else:  #if update operation
            writers = Writers.objects.get(pk=id)   #get the id parameter from url
            form = WritersForm(request.POST,instance=writers)   #update the data from the recent input and update the data.
        # check whether it's valid:
        if form.is_valid():
            # If form is validated, submit it.
            form.save()
            # then redirect to a new URL which is the list:
            return redirect('/writers/list/')

    # if a GET (or any other method) we'll create a blank form
    else:
        if id==0:
            form = WritersForm()
        else:
            writers = Writers.objects.get(pk=id)
            form = WritersForm(instance=writers)
    return render(request,"writer_register/writers_form.html",{'form':form})

def writers_delete(render,id):
    writers = Writers.objects.get(pk=id)
    writers.delete()
    return redirect('/writers/list')