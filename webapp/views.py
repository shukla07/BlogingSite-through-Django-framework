from django.shortcuts import render
from django.http import HttpResponse

def index(response):
	return HttpResponse("<h2>Hey!</h2>")
