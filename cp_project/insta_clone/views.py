from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("home view")







# for the search, one text entry field; Q objects to do or on all the User fields

# create middleware to require login on all pages

# reference trwibc (on flash drive) for file uploads
# Photos should be its own model (keys to User)
