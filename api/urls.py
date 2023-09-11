from django.urls import path
from .views import TaskView

urlpatterns = [
    path('api/', TaskView.as_view()),


]

