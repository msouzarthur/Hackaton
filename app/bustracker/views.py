from django.shortcuts import render, redirect
from django.template import loader
import random

from datetime import date
from .models import RouteStop, Stop, Route, Reservation, Bus, Driver

def index(request):
	bus = Bus.objects.all()
	context = {
		'bus': bus
	}
	return render(request, 'index.html', context)

def motorista(request):
	#random number between 0 and 5
	r = random.randint(0, 4)
	drivers_name = [ _driver.driver_name for _driver in Driver.objects.all()]
	img = ['https://i.imgur.com/L4pefCl.jpg','https://i.imgur.com/ySlOeIp.png','https://i.imgur.com/yJ6uAk8.png','https://i.imgur.com/m7tP7WU.png', 'https://i.imgur.com/EVPPwnW.png']
	id_num = [10525, 10526, 10527, 10528, 10529]
	context = {
		'driver_name': drivers_name[r],
		'id_num': id_num[r],
		'perfil': img[r],
	}
	return render(request, 'motorista.html', context)

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
	context = {
		'routes': Route.objects.all().filter(route_est_time),
		'stops': Stop.objects.all(),
		'reservations': Reservation.objects.all()
	}
	return render(request, 'estatisticas.html',context)