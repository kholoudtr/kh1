from django.shortcuts import render
from django.http import HttpResponse
from .models import Carv
# Create your views here.
def index(request):
      return render(request,'car/index.html',{'car':Carv.objects.all()})

def about(request):
      return render(request,'car/about.html')


def contact(request):
      return render(request,'car/contact.html')