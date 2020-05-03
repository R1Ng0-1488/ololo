from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def lol(request):
	return HttpResponse('<h1>OLOLO</h1>')