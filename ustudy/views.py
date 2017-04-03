def home(request):
	context = () #empty dictionary
	return render (request, 'templates/base.html')