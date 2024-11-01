from django.urls import path
from . import views
urlpatterns = [

    path('', views.tu_vista, name='index'),
    path('modulo/<int:numero>/', views.modulo, name='modulo'),
    
]