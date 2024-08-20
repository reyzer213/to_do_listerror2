from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, SignUpView

urlpatterns = [
    # Список завдань
    path('', TaskListView.as_view(), name='task_list'),  

    # Деталі завдання
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),  

    # Створення нового завдання
    path('task/new/', TaskCreateView.as_view(), name='task_create'),

    # Редагування завдання
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),

    # Видалення завдання
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),

    path('signup/', SignUpView.as_view(), name='signup'),
]

#path('project/<int 😛 k>/',  
# ProjectDetailView.as_view(), 
#  name='project_detail') 
