from django.shortcuts import render

def catgories(request):
    # Your view logic here
    return render(request,'catgories/catgory.html')