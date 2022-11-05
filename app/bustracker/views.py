from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Stop
# Create your views here.
def index(request):
	return render(request, 'index.html')
    #return HttpResponse("Hello, world. You're at the bus tracker index.")
