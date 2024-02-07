from django.urls import path,include

from . import views
urlpatterns = [
  path('',include('django.contrib.auth.urls')),
  path('profile/',views.Myprofile,name='myprofile'),
  path('register/',views.Registrationform.as_view()),
  
   
]
