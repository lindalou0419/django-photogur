from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.urls import path, reverse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from photogur.models import Picture, Comment
from photogur.forms import PictureForm

# import pdb

def root(request):
  return HttpResponseRedirect('pictures')
#------------------------------------------


def picture(request):
  context = {
    'pictures': Picture.objects.all(),
    'title': 'Django Photogur',
  }
  response = render(request, 'pictures.html', context)
  return HttpResponse(response)
#------------------------------------------


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
#------------------------------------------


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
#------------------------------------------


@login_required
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
#------------------------------------------


def signup(request):
  form = UserCreationForm()
  context = {'form': form}
  response = render(request, 'registration/signup.html', context)
  return HttpResponse(response)
#------------------------------------------


def signup_create(request):
  form = UserCreationForm(request.POST)
  if form.is_valid():
    new_user = form.save()
    # @TODO
    login(request, new_user)
    return redirect('pictures')
  else:
    context = {'form': form}
    response = render(request, 'registration/signup.html', context)
    return HttpResponse(response)
#------------------------------------------


@login_required
def picture_new(request):
  form = PictureForm()
  context = {
    'form': form,
    'title': 'Add a New Picture',
  }
  response = render(request, 'pictures/new.html', context)
  return HttpResponse(response)
#------------------------------------------


@login_required
def picture_create(request):
  form = PictureForm(request.POST)
  if form.is_valid():
    form.save()
    return redirect('pictures')
  else:
    context = {'form': form}
    return render(request, 'products/new.html', context)
#------------------------------------------
