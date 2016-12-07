from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context_dict = {'boldmessage': "Crunchy, creamy, cookie dough..."}
	return render(request, 'rango/index.html', context=context_dict)
	# return HttpResponse("Rango says: Yo! <br/>Also, Do check out our <a href='/about'>about</a> page.")

def about(request):
	return HttpResponse("Rango says: this be the about page! <br/>Or go to the <a href='/rango'>Home Page</a>")