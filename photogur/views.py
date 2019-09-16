from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from photogur.models import Picture

def root(request):
  return HttpResponseRedirect('pictures')

def picture(request):
  context = {'pictures': Picture.objects.all()}
  response = render(request, 'pictures.html', context)
  return HttpResponse(response)