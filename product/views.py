from django.shortcuts import render,reverse,redirect
from django.http import  HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *
from .formsModel import *
from django.views import View
from django.views.generic import UpdateView,DetailView,DeleteView,ListView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

def hello(request):
    return  render(request,'index.html')
class ProductAddGeneric(CreateView):
    model = Product
    template_name = 'product/addFormModel.html'
    form_class = ProductFormModel
    success_url = reverse_lazy('product.listFormModel')

class ProductListGeneric(ListView):
    model = Product
    template_name = 'product/index.html'
    context_object_name = 'products'
    success_url = reverse_lazy('product.listFormModel')

class ProductDeleteGeneric(DeleteView):
    model = Product
    template_name = 'product/deleteFormModel.html'
    success_url = reverse_lazy('product.all')

class ProductDetailsGeneric(DetailView):
    model = Product
    template_name = 'product/details.html'
    context_object_name = 'product'

class ProductUpdateGeneric(UpdateView):
    model = Product
    template_name = 'product/updateFormModel.html'
    context_object_name = 'formModel'
    form_class = ProductFormModel
    success_url = reverse_lazy('product.all')

class ProductUpdate(View):
    def get(self, request, id):
        context = {'formModel': ProductFormModel(instance=Product.productDetails(id))}
        return render(request,'product/UpdateFormModel.html',context)

    def post(self, request, id):
        formModel = ProductFormModel(request.POST,request.FILES,instance=Product.productDetails(id))
        if (formModel.is_valid()):
            formModel.save()
            return redirect(reverse('product.all'))

def productUpdateFormModel(request,id):
    # updatedproduct=Product.productDetails(id)
    context = {'formModel': ProductFormModel(instance=Product.productDetails(id))}
    if request.method == 'POST':
        formModel = ProductFormModel(request.POST,request.FILES,instance=Product.productDetails(id))
        if (formModel.is_valid()):
            formModel.save()
            return redirect(reverse('product.all'))
    return render(request,'product/UpdateFormModel.html',context)
    
@login_required()
def productUpdate(request,id):
    # product=Product.objects.get(id=id)
    product=Product.productDetails(id)
    context={'product':product}
    if request.method == 'POST':
            if (request.POST['pName'] != ''):
                Product.productUpdate(request,id)
                # Product.objects.filter(id=id).update(
                #                 name=request.POST['pName'],
                #                 price=request.POST['pPrice'],
                #                 description=request.POST['pDescription'],
                #                 count=request.POST['pCount']
                #                 )

# Update Product Image
                # obj = Product.objects.get(id=id)
                # obj.name = request.POST['pName']
                # obj.price = request.POST['pPrice']
                # obj.description = request.POST['pDescription']
                # obj.count = request.POST['pCount']
                # obj.image = '/product/images/'+request.POST['pImage']
                # obj.save()
                return HttpResponseRedirect(reverse('product.all'))
            else:
                context['msg']='Kindly fill all fields'
    context['categories']=Category.objects.all()
    return render(request,'product/update.html',context)
# if request.method == 'POST':
#         Product.productAdd(request)
#         # Product.objects.create(name=request.POST['pName'],
#         #                        price=request.POST['pPrice'],
#         #                        description=request.POST['pDescription'],
#         #                        image=request.FILES['pImage'],
#         #                        count=request.POST['pCount']
#         #                        )
#         return HttpResponseRedirect(reverse('product.all'))
#     context={'categories':Category.objects.all()}
#     return render(request,'product/add.html',context)

@login_required()
def productDelete(request,id):
    # Product.objects.filter(id=id).delete()
    Product.productDelete(id)
    return HttpResponseRedirect(reverse('product.all'))

def productAddFormModel(request):
    formModel = ProductFormModel()
    context = {'formModel': formModel}
    if request.method == 'POST':
        formModel = ProductFormModel(request.POST,request.FILES)
        if (formModel.is_valid()):
            formModel.save()
            return HttpResponseRedirect(reverse('product.all'))
    return render(request,'product/addFormModel.html',context)

def productAddForm(request):
    form = ProductForm()
    context = {'form': form}
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if (form.is_valid()):
            # Product.productAdd(request) ==>Must be handled first to be dynamic for gui and forms
            Product.objects.create(name=request.POST['name'],
                                price=request.POST['price'],
                                description=request.POST['description'],
                                image=request.FILES['image'],
                                count=request.POST['count'],
                                category=Category.objects.get(id=request.POST['category'])
                                
                                )
            return HttpResponseRedirect(reverse('product.all'))
        else:
            context['msg'] = 'Data not completed'
    return render(request,'product/addForm.html',context)

@login_required()
def addProduct(request):
    if request.method == 'POST':
        Product.productAdd(request)
        # Product.objects.create(name=request.POST['pName'],
        #                        price=request.POST['pPrice'],
        #                        description=request.POST['pDescription'],
        #                        image=request.FILES['pImage'],
        #                        count=request.POST['pCount']
        #                        )
        return HttpResponseRedirect(reverse('product.all'))
    context={'categories':Category.objects.all()}
    return render(request,'product/add.html',context)

def productList(request):
    # context={'products':Product.objects.all()}
    context={'products':Product.productsList()}
    return  render(request,'product/index.html',context)

def productdetails(request,productid):
    # obj=Product.objects.get(id=productid)
    obj=Product.productDetails(productid)
    context={'product':obj}
    # context={'product':Product.objects.get(id=productid)}
    return  render(request,'product/details.html',context)

def aboutUs(request):
    return  render(request,'aboutUs.html')