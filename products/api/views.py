from rest_framework import views
from rest_framework.response import Response
#from django.http.response import jasonResponse
from rest_framework.decorators import api_view
@api_view(['GET'])
def Hello(request):
  return Response({'msg':'hello our customer'})
  #return jasonResponse({})


