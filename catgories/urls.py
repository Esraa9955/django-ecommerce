from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns=[
   path('',views.categorylist,name='category.all'),
   path('Add/',views.categoryadd,name='category.add'),
   path('update/<int:pk>',views.CategoryUpdategeneric.as_view(),name="category.Update"),
   path('<int:pk>',views.CategoryDetailsgeneric.as_view(),name="category.details"),
   path('delete/<int:pk>',views.CategoryDeletegeneri.as_view(),name="category.delete"),
   path('List/',views.CategoryListgeneric.as_view(), name='category.glist'),
   #path('update/<int:id>',views.CategoryUpdateView.as_view(),name="category.Update"),
   #path('update/<int:id>',views.CategoryUpdate,name="category.Update"),
]

