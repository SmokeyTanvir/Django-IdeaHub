from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from .models import Idea
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        idea = request.POST.get("new-idea-input")

        # checking if opinion is empty
        if len(idea) == 0:
            return render(request, "Ideas/index.html", {
                'message': 'Error...Idea cannot be empty'
            })

        # if task is not empty
        new_idea = Idea(idea=idea, author=request.user)
        new_idea.save()

        # Redirect to the index view using the GET method
        return redirect('index')



    if not request.user.is_authenticated:
        return redirect('login')


    ideas = Idea.objects.all()

    return render(request, "Ideas/index.html", {
        "ideas": ideas
    })

# view for deleting an idea
def delete_idea(request, ideaID):
    try: 
        idea_to_delete = Idea.objects.get(id=ideaID)
        idea_to_delete.delete()
        return JsonResponse({'message': 'idea deleted successfully'})
    except Idea.DoesNotExist:
        return JsonResponse({'message': 'ERROR...idea does not exist'})

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
            return render(request, "Ideas/login.html", {
                "message": "Invalid username and/or password."
            })

    if request.user.is_authenticated:
        return redirect(reverse("index"))

    return render(request, "Ideas/login.html")

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


    return render(request, "Ideas/register.html", {
        'form' : form
        })