from django.urls import path
from . import views
urlpatterns=[
 path('',views.products, name='products'),
 path('<int:id>',views.product, name='product'),
 path('New',views.productadd,name='product.add'),
 path('Delete/<int:id>',views.productdelete,name='product.delete'),

]
