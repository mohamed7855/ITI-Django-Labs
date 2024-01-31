from django.urls import path
from . import  views
urlpatterns = [
    path('List',views.productList),
    path('<int:productid>',views.productdetails,name="product.details"),
    path('Category',views.productList),
]