from django.conf.urls import url
from stolarnia import views

urlpatterns = [
    url(r'^status/', views.status, name='status'),
    url(r'^przekaz/', views.status, name='przekaz'),
]
