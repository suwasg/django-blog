from django.shortcuts import render
from django.http import HttpResponse
from django.views .generic import ListView, CreateView,DetailView,UpdateView,DeleteView

# Create your views here.
# 2 -> FBV,CBV (function base views, )

#Function Base Views
def index(request):
    return HttpResponse("You're at the blog index")
def about(request):
    return HttpResponse("You're at the blog about.")
def blog(request):
     return HttpResponse("You're at the blog.")
def singleblog(request):
     return HttpResponse("You're at the single blog.")
def contact(request):
      return HttpResponse("You're at the contact.")
def getSingleCategory(request):
      return HttpResponse("You're at the blog getSingleCategory.")