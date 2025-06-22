from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.generate_qr_code, name='generate_qr_code'),
]
