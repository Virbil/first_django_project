from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("placeholder for landing page in User")

def register(request):
    if request == '/register':
        return HttpResponse("placeholder for users to create a new user record")
    else:
        return HttpResponse("placeholder for users/new endpoint")


def log_in(request):
    return HttpResponse("placeholder for users to log in")

def list_users(request):
    return HttpResponse("placeholder to later display all the list of users")