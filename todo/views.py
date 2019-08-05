from django.shortcuts import render, redirect #we want to redirect to another page after function
from .models import List #added
from .forms import ListForm
from django.contrib import messages #we can pass messages whenever we add/remove objects
# Create your views here.
def home(request):
    #will direct you home
    return render(request,'todo/home.html')

def create(request):
    #if someone has info and adds it go through this
    if request.method == "POST":
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            #list all objects in database, we can access through dictionary at the bottom
            all_items = List.objects.all
            #when we add
            messages.success(request, ("item has been added"))
                                                        #dictionary
            return render(request, 'todo/create.html',{'all_items': all_items})

    else:
        #other wise just show the page
        all_items = List.objects.all
        return render(request, 'todo/create.html',{'all_items': all_items})

def delete(request, list_id):
    #we want to set that item to id number
    item= List.objects.get(pk=list_id)
    #delete
    item.delete()
    messages.success(request,('Item has been deleted'))
    return redirect('create')


def cross_off(request,list_id):
    #we want to set that item to id number
    item= List.objects.get(pk=list_id)
    #change completed form False to True, True that is has been crossed off
    item.completed = True
    item.save()
    return redirect('create')

def uncross(request,list_id):
    #we want to set that item to id number
    item= List.objects.get(pk=list_id)
    #change completed to False becouse its been crossed of
    item.completed = False
    item.save()
    return redirect('create')

def edit(request, list_id):
    if request.method == "POST":
        item = List.objects.get(pk=list_id)

        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ('item has been edited'))
            return redirect('create')

    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'todo/edit.html',{'item':item})
