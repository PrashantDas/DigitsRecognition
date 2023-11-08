from django.urls import path
from .views import one_view, methodology

urlpatterns = [
    path('', one_view, name='home'),
    path('methodology/', methodology, name='methodology')
]