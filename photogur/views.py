from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def root(request):
  return HttpResponseRedirect('pictures')

def picture(request):
  response = render(request, 'pictures.html')
  return HttpResponse(response)