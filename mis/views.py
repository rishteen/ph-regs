from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Employee


def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'mis/employee_detail.html', {'employee': employee})
