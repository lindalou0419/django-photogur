from django.contrib import admin
from django.urls import path, include
from photogur import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.root, name="index"),
  path('pictures/', views.picture, name="pictures"),
  path('pictures/<int:pic_id>/', views.picture_show, name='picture_details'),
  path('pictures/new/', views.picture_new, name='picture_new'),

  path('search/', views.picture_search, name='picture_search'),
  path('comments/new/', views.comment_create, name='comment_create/'),

  path('accounts/signup/', views.signup, name='signup'),
  path('accounts/signup_create/', views.signup_create, name='signup_create'),
  path('accounts/', include('django.contrib.auth.urls')),
]
