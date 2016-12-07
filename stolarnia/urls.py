from django.conf.urls import url
from szwalnia import views

urlpatterns = [
    url(r'^status/', views.status, name='status'),
    url(r'^przekaz/', views.status, name='przekaz'),
]
