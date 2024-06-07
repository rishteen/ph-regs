from .views import employee_detail
from django.urls import path
from . import views

app_name = 'mis'

urlpatterns = [
    path('employee/<int:pk>/', employee_detail, name='employee_detail'),
]
