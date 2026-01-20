
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.shortcuts import render
from .models import Student
import json
import requests

import requests
from requests.exceptions import RequestException

def random_student(request):
    weather_data = {}

    try:
        response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": 18.52,
                "longitude": 73.85,
                "current_weather": "true"
            },
            timeout=5
        )
        response.raise_for_status()
        data = response.json()

        weather = data.get("current_weather", {})

        weather_data = {
            "city": "Pune",
            "temperature": weather.get("temperature"),
            "windspeed": weather.get("windspeed"),
            "winddirection": weather.get("winddirection"),
            "time": weather.get("time"),
        }

    except RequestException as e:
        print("Weather API error:", e)
        weather_data = {
            "city": "Unavailable",
            "temperature": "N/A",
            "windspeed": "N/A",
            "winddirection": "N/A",
            "time": "N/A",
        }

    return render(request, "random_students.html", {"weather": weather_data})

def dashboard(request):
    total_students = Student.objects.count()
    status_data = Student.objects.values('status').annotate(count=Count('id'))

    trend_queryset = (
        Student.objects
        .annotate(date=TruncDate('created_at'))
        .values('date')
        .annotate(count=Count('id'))
        .order_by('date')
    )

    trend_labels = [str(item['date']) for item in trend_queryset] or []
    trend_counts = [item['count'] for item in trend_queryset] or []

    context = {
        'total_students': total_students,
        'status_data': status_data,
        'trend_labels': json.dumps(trend_labels),
        'trend_counts': json.dumps(trend_counts),
    }
    return render(request, 'dashboard.html', context)

def home(request):
    return render(request, 'home.html')

# LIST STUDENTS
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


# CREATE STUDENT
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'student_form.html', {'form': form})


# UPDATE STUDENT
def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'student_form.html', {'form': form})


# DELETE STUDENT
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        
        return redirect('student_list')

    return render(request, 'student_confirm_delete.html', {'student': student})
