from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
   
    s='<h1>welcome bubu</h1>'
    return HttpResponse(s)