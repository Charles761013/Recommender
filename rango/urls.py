from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^about/$', views.about, name='about'),
    url(r'^$', views.index, name='index'),
    url(r'^map$', views.google_map, name='google_map'),
    
  
]