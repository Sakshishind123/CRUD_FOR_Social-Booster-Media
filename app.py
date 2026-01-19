import webbrowser
from django.apps import AppConfig
import threading

class EventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'events'

    def ready(self):
        def open_browser():
            webbrowser.open_new('http://127.0.0.1:8000/student_list.html/')  # Replace with your URL path
        threading.Timer(1.5, open_browser).start()
