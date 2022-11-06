from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from datetime import date
from .models import RouteStop, Stop, Route

def index(request):
	#return render()
	return HttpResponse('hello')

def motorista(request):
	return render(request, 'motorista.html')

def agendamento(request, route=""):
	routes = [ _route.route_name for _route in Route.objects.all() ]
	routes.append('Selecionar rota')
	context = {
			'routes': routes
		}

	if request.method == "POST":
		context.update({'selected_route':request.POST.get('route'),
					'date':request.POST.get('date'),
					'routestops':RouteStop.objects.all().filter(route__route_name=request.POST.get('route'))
				})
		return render(request, 'agendamento.html', context)

	context.update({'date': date.today().isoformat(),
				'selected_route':"Selecionar rota",
				'routestops':RouteStop.objects.all()
			})
	return render(request, 'agendamento.html', context)

def registrar(request):
	return render(request, 'registrar.html')

def entrar(request):
	return render(request, 'entrar.html')