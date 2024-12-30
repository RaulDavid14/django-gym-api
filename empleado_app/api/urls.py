from django.urls import path
from empleado_app.api.views import *

urlpatterns = [
    path('', EmpleadoAV.as_view(), name='empleado'),
    
]
