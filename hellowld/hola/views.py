from django.shortcuts import render
from django.http import HttpResponse

def spain(request):
	return HttpResponse('Hola is HELLO in Spanish')

def india(request):
	return HttpResponse('Namaste is HELLO in Hindi')
