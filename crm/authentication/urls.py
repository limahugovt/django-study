from django.urls import path
from .views import ViewLogin

urlpatterns = [
    path('login', name='login', view=ViewLogin),
]
