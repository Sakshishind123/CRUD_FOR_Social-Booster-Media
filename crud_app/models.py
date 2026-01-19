# from django.db import models

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone=models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

from django.db import models

class Student(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
