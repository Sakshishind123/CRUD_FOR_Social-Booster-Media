
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.shortcuts import render
from .models import Student
import json
import requests
from django.shortcuts import render

def random_student(request):
    response = requests.get('https://randomuser.me/api/?results=10&nat=us')  # get 5 random users
    data = response.json()
    students = []
    for user in data['results']:
        students.append({
            'name': f"{user['name']['first']} {user['name']['last']}",
            'email': user['email'],
            'phone': user['phone'],
            'country': user['location']['country'],
            'picture': user['picture']['medium'],
        })
    return render(request, 'random_students.html', {'students': students})

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
