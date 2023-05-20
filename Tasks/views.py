from django.shortcuts import render, redirect  
from .models import Task  
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse 

# Create your views here.

def index(request):
    if request.method == 'POST':
        task_name = request.POST.get("new-task-input")

        # checking if task is empty
        if len(task_name) == 0:
            return render(request, "Tasks/index.html", {
                'message': 'Error...Task cannot be empty'
            })

        # if task is not empty
        new_task = Task(task_name=task_name)
        new_task.save()

        # Store a success message in the session
        request.session['task_added_message'] = 'Your task has been submitted for authorization'

        # Redirect to the index view using the GET method
        return redirect('index')

    tasks = Task.objects.all()

    # Retrieve the task_added_message from the session
    task_added_message = request.session.pop('task_added_message', None)

    return render(request, "Tasks/index.html", {
        "tasks": tasks,
        "task_added_message": task_added_message
    })


def delete_task(request, taskID):
	try: 
		task_to_delete = Task.objects.get(id=taskID)
		task_to_delete.delete()
		return JsonResponse({'message': 'task deleted successfully'})
	except Task.DoesNotExist:
		return JsonResponse({'message': 'ERROR...task does not exist'})