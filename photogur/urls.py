from django.contrib import admin
from django.urls import path
from photogur import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.root, name="index"),
  path('pictures/', views.picture),
  path('pictures/<int:pic_id>', views.picture_show, name='picture_details'),
]
