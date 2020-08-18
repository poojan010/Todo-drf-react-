from django.urls import path
from . import views


urlpatterns = [
	path('',views.apiOverview, name='api-overview'),
	path('task-list/',views.taskList, name='task-list'),
	path('task-create/',views.taskCreate, name='task-create'),
	path('task-detail/<str:primarykey>/',views.taskDetail, name='task-detail'),
	path('task-update/<str:primarykey>/',views.taskUpdate, name='task-update'),
	path('task-delete/<str:primarykey>/',views.taskDelete, name='task-delete'),
]