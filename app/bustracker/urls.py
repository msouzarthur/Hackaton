from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('motorista', views.motorista, name='motorista'),
	path('agendamento', views.agendamento, name='agendamento'),
	path('registrar', views.registrar, name='registrar'),
	path('entrar', views.entrar, name='entrar')
]