from django.shortcuts import render

# Create your views here.
def filter(request):
    d={'data':'NevEr GivE up'}
    return render(request,'filter.html',d)