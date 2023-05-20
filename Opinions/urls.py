from django.urls import path 
from . import views 


urlpatterns = [
	path("", views.index, name="index"),
	path("delete/<int:opinionID>", views.delete_opinion, name="delete_opinion")
]