from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from .models import Opinion

# Create your views here.

def index(request):
    if request.method == 'POST':
        opinion_name = request.POST.get("new-opinion-input")

        # checking if opinion is empty
        if len(opinion_name) == 0:
            return render(request, "Opinions/index.html", {
                'message': 'Error...Task cannot be empty'
            })

        # if task is not empty
        new_opinion = Opinion(opinion=opinion_name)
        new_opinion.save()

        # Store a success message in the session
        request.session['opinion_added_message'] = 'Your opinion has been submitted for authorization'

        # Redirect to the index view using the GET method
        return redirect('index')

    opinions = Opinion.objects.all()

    # Retrieve the task_added_message from the session
    opinion_added_message = request.session.pop('opinion_added_message', None)

    return render(request, "Opinions/index.html", {
        "opinions": opinions,
        "opinion_added_message": opinion_added_message
    })


def delete_opinion(request, taskID):
	try: 
		opinion_to_delete = Opinion.objects.get(id=opinionID)
		opinion_to_delete.delete()
		return JsonResponse({'message': 'opinion deleted successfully'})
	except Opinion.DoesNotExist:
		return JsonResponse({'message': 'ERROR...opinion does not exist'})