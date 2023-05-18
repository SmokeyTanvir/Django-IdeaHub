from django.shortcuts import render
from .models import Task  
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse 

# Create your views here.
def index(request):
	tasks = Task.objects.all()
	return render(request, "Tasks/index.html", {
		"tasks": tasks
		})

def add_task(request):
	if request.method == 'POST':
		task_name = request.POST.get("new_task")
		new_task = Task(task_name=task_name)
		new_task.save()
		return  HttpResponseRedirect(reverse("index"))

	return render(request, "Tasks/add.html")


def delete_task(request, taskID):
	try: 
		task_to_delete = Task.objects.get(id=taskID)
		task_to_delete.delete()
		return JsonResponse({'message': 'task deleted successfully'})
	except Task.DoesNotExist:
		return JsonResponse({'message': 'ERROR...task does not exist'})