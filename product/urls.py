from django.urls import path
from . import  views
urlpatterns = [
    path('',views.productList,name="product.all"),
    path('<int:productid>',views.productdetails,name="productDetails"),
    path('New',views.addProduct,name="productAdd"),
    path('NewForm',views.productAddForm,name="product.addForm"),
    path('Delete/<int:id>',views.productDelete,name="product.delete"),
    path('Update/<int:id>',views.productUpdate,name="product.update"),
    # Form Model
    path('NewFormModel',views.productAddFormModel,name="product.addFormModel"),
]