# # from django.http import JsonResponse
# # from .models import Student
# # from django.views.decorators.csrf import csrf_exempt
# # import json

# # @csrf_exempt
# # def student_list(request):
# #     if request.method == 'GET':
# #         students = list(Student.objects.values())
# #         return JsonResponse(students, safe=False)
# #     elif request.method == 'POST':
# #         data = json.loads(request.body)
# #         student = Student.objects.create(**data)
# #         return JsonResponse({'message': 'Student created', 'id': student.id})

# # @csrf_exempt
# # def student_detail(request, id):
# #     try:
# #         student = Student.objects.get(id=id)
# #     except Student.DoesNotExist:
# #         return JsonResponse({'error': 'Student not found'}, status=404)

# #     if request.method == 'GET':
# #         return JsonResponse({'id': student.id, 'name': student.name, 'email': student.email, 'phone': student.phone})
# #     elif request.method == 'PUT':
# #         data = json.loads(request.body)
# #         student.name = data.get('name', student.name)
# #         student.email = data.get('email', student.email)
# #         student.phone = data.get('phone', student.phone)
# #         student.save()
# #         return JsonResponse({'message': 'Student updated'})
# #     elif request.method == 'DELETE':
# #         student.delete()
# #         return JsonResponse({'message': 'Student deleted'})
# from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import Student
# from .forms import StudentForm
# import json
# def student_list_page(request):
#     students = Student.objects.all()
#     return render(request, 'student_list.html', {'students': students})
# @csrf_exempt
# def student_list_api(request):
#     if request.method == 'GET':
#         students = list(Student.objects.values())
#         return JsonResponse(students, safe=False)

#     elif request.method == 'POST':
#         data = json.loads(request.body)
#         student = Student.objects.create(**data)
#         return JsonResponse({'message': 'Student created', 'id': student.id})
# @csrf_exempt
# def student_detail_api(request, id):
#     student = get_object_or_404(Student, id=id)

#     if request.method == 'GET':
#         return JsonResponse({
#             'id': student.id,
#             'name': student.name,
#             'email': student.email,
#             'phone': student.phone
#         })

#     elif request.method == 'PUT':
#         data = json.loads(request.body)
#         student.name = data.get('name', student.name)
#         student.email = data.get('email', student.email)
#         student.phone = data.get('phone', student.phone)
#         student.save()
#         return JsonResponse({'message': 'Student updated'})

#     elif request.method == 'DELETE':
#         student.delete()
#         return JsonResponse({'message': 'Student deleted'})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
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
