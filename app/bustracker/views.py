from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

from datetime import date
from .models import RouteStop, Stop, Route, Reservation, Bus

def index(request):
	bus = Bus.objects.all()
	context = {
		'bus': bus
	}
	return render(request, 'index.html', context)

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

def entrar(request):
	return render(request, 'entrar.html')

def reservar(request, id:int):
	#Reservation.objects.create(reservation_passenger=1, reservation_bus=1, )
	return redirect('agendamento')

def estatisticas(request):
	return render(request, 'estatisticas.html')