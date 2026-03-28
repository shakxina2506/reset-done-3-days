from django.urls import path
from .views import home,active_tasks

urlpatterns = [
    path('', home, name='home'),
    path('active_tasks/', active_tasks, name='active_tasks'),
]