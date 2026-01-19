# # from django.urls import path
# # from . import views

# # urlpatterns = [
# #     path('', views.student_list, name='student_list'),  # matches /crud_app/
# #     path('students/<int:id>/', views.student_detail, name='student_detail'),  # matches /crud_app/students/1/
# # ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     # HTML page
#     path('', views.student_list_page, name='student_list'),

#     # API endpoints
#     path('api/students/', views.student_list_api),
#     path('api/students/<int:id>/', views.student_detail_api),
# ]

from django.urls import path
from . import views

urlpatterns = [
      path('', views.home, name='home'),
       path('dashboard/', views.dashboard, name='dashboard'),
path('random-students/', views.random_student, name='random_student'),

     path('students/', views.student_list, name='student_list'),
    path('create/', views.create_student, name='create_student'),
    path('update/<int:id>/', views.update_student, name='update_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
]

