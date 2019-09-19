from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.urls import path, reverse
from photogur.models import Picture, Comment

# import pdb

def root(request):
  return HttpResponseRedirect('pictures')

def picture(request):
  context = {
    'pictures': Picture.objects.all(),
    'title': 'Django Photogur',
  }
  response = render(request, 'pictures.html', context)
  return HttpResponse(response)

def picture_show(request, pic_id):
  picture = Picture.objects.get(id=pic_id)
  comments = picture.comments.order_by("-created_at")
  context = {
    'picture': picture,
    'comments': comments,
    'title': picture.title,
  }
  response = render(request, 'picture.html', context)
  return HttpResponse(response)

def picture_search(request):
  query = request.GET['query']
  search_results = Picture.objects.filter(artist=query)
  context = {
    'pictures': search_results,
    'title': 'Search Results',
    'query': query
  }
  response = render(request, 'results.html', context)
  return HttpResponse(response)

@require_http_methods(['POST'])
def comment_create(request):
  name = request.POST['poster-name']
  message = request.POST['poster-comment']
  picture_id = request.POST['picture-id']
  picture = Picture.objects.get(id=picture_id)

  Comment.objects.create(
    name = name,
    message = message,
    picture = picture
  )

  return redirect('picture_details', picture.id)
  # return HttpResponseRedirect(reverse('picture_details', args=[picture.id]))