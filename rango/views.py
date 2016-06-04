from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

def about(request):
    return render(request, 'rango/about.html', {})
    #return HttpResponse("This is the about page.")
    
def index(request):
    return render(request, 'rango/index.html', {})
    
