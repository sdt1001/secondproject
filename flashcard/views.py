from django.shortcuts import render

# Create your views here.
def home(request):
	context = [] #empty context dictionary
	return render(request, 'flashcard/home.html', context)