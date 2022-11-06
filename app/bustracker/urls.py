from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('motorista', views.motorista, name='motorista'),
	path('agendamento', views.agendamento, name='agendamento'),
	path('entrar', views.entrar, name='entrar'),
	path('reservar/<int:id>', views.reservar, name='reservar'),
	path('estatisticas', views.estatisticas, name='estatisticas')
]