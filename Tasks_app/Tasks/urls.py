from django.urls import path 
from . import views 


urlpatterns = [
	path("", views.index, name="index"),
	path("add", views.add_task, name="add"),
	path("delete/<int:taskID>", views.delete_task, name="delete_task")
]