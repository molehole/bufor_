from django.conf.urls import url
from agregator import views

urlpatterns = [
    url(r'^status/', views.status, name='status'),
    url(r'^przekaz/', views.status, name='przekaz'),
    url(r'^oddaj/', views.status, name='oddaj'),
    url(r'^potwierdz/', views.status, name='potwierdz'),
    url(r'^sprawdz/', views.status, name='sprawdz'),
]
