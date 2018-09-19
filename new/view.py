from django.http import HttpResponse
from django.shortcuts import render

def search_form(request):
	context = {}
	return render(request,"search.html",context)
def search(request):
	context = {}
	if 'q' in request.GET:
		context['hello'] = request.GET['q'];
		return render(request,"hello.html",context)
	else:
		context['hello'] = "nothing"
		return render(request,"hello.html",context)
def login(request):
	return render(request,"ddd.html")