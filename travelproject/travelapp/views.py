from django.http import HttpResponse
from django.shortcuts import render
from . models import Place,Team

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1 = Team.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obj1})



# def addition(request):
#     a=int(request.GET['num1'])
#     b=int(request.GET['num2'])
#     res=a+b
#     return render(request,"about.html",{'result':res})
