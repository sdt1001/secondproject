from django.shortcuts import render

def home(request):
	context = () #empty dictionary
	return render (request, 'base.html')