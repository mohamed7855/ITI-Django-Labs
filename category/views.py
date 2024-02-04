from django.shortcuts import render,reverse
from django.http import  HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.

def categoryUpdate(request,id):
    category=Category.objects.get(id=id)
    context={'category':category}
    if request.method == 'POST':
            if (request.POST['cName'] != ''):
                Category.objects.filter(id=id).update(
                                name=request.POST['cName'],
                                email=request.POST['cEmail'],
                                image=request.POST['cImage'],
                                age=request.POST['cAge'],
                                )
                return HttpResponseRedirect(reverse('category.all'))
            else:
                context['msg']='Kindly fill all fields'
    return render(request,'category/update.html',context)
    
def categoryDelete(request,id):
    Category.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('category.all'))

def categoryAddForm(request):
    form = CategoryForm()
    context = {'form': form}
    if request.method == 'POST':
        form = CategoryForm(request.POST,request.FILES)
        if (form.is_valid()):
            Category.objects.create(name=request.POST['name'],
                                email=request.POST['email'],
                                image=request.FILES['image'],
                                age=request.POST['age']
                                )
            return HttpResponseRedirect(reverse('category.all'))
        else:
            context['msg'] = 'Data not completed'
    return render(request,'category/addForm.html',context)

def addCategory(request):
    if request.method == 'POST':
        Category.objects.create(name=request.POST['cName'],
                                email=request.POST['cEmail'],
                                image=request.FILES['cImage'],
                                age=request.POST['cAge']
                               )
        return HttpResponseRedirect(reverse('category.all'))
    return render(request,'category/add.html')

def categoryList(request):
    context={'categories':Category.objects.all()}
    return render(request,'category/index.html',context)

def categorydetails(request,id):
    obj=Category.objects.get(id=id)
    context={'category':obj}
    # context={'category':Category.objects.get(id=id)}
    return  render(request,'category/details.html',context)