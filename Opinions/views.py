from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from .models import Opinion
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm


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
        new_opinion = Opinion(opinion=opinion_name, user=request.user)
        new_opinion.save()

        # Redirect to the index view using the GET method
        return redirect('index')



    if not request.user.is_authenticated:
        return redirect('login')


    opinions = Opinion.objects.all()

    return render(request, "Opinions/index.html", {
        "opinions": opinions
    })

# view for deleting an opinion
def delete_opinion(request, opinionID):
    try: 
        opinion_to_delete = Opinion.objects.get(id=opinionID)
        opinion_to_delete.delete()
        return JsonResponse({'message': 'opinion deleted successfully'})
    except Opinion.DoesNotExist:
        return JsonResponse({'message': 'ERROR...opinion does not exist'})

# view for user login
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return redirect(reverse("index"))
        else:
            return render(request, "Opinions/login.html", {
                "message": "Invalid username and/or password."
            })

    if request.user.is_authenticated:
        return redirect(reverse("index"))

    return render(request, "Opinions/login.html")

# view for user logout
def logout_view(request):
    logout(request)
    return redirect(reverse("login"))

# view for registration (new user)
def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            opinion = form.save(commit=False)
            opinion.user = request.user
            opinion.save()
            return redirect('login')
    else:
        form = SignupForm()


    return render(request, "Opinions/register.html", {
        'form' : form
        })