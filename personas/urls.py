from django.urls import path
from . import views


urlpatterns = [

    path('lista/',views.personalist,name='persona_lista'),
    
]
