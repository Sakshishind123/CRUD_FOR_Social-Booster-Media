# from django.contrib import admin
# from django.urls import include, path

# urlpatterns = [
#     path('admin/', admin.site.urls),
    
#     path('crud_app/', include('crud_app.urls')),

# ]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crud_app.urls')),  # 👈 ROOT URL
]
