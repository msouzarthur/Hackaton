from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from datetime import date
from .models import RouteStop

def index(request, route=""):
	if request.method == "POST":
		context = {'selected_route':request.POST.get('route'),
					'routes':['Selecionar rota', 'anglo - ru', 'anglo - famed'],
					'date':request.POST.get('date'),
					'routestops':RouteStop.objects.filter()
				}
		return render(request, 'index.html', context)
	print(RouteStop.objects)
	context = {'date': date.today().isoformat(),
				'selected_route':"Selecionar rota",
				'routes': ['Selecionar rota', 'Anglo', 'Capão do Leão'],
				'routestops':RouteStop.objects.all()
				}
	return render(request, 'index.html', context)

def onibus(request):
	return HttpResponse("Entrei no aluninho onibus")