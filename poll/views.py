from django.shortcuts import render
from .forms import PollModelForm
from .models import Poll
# Create your views here.

def home_view(request):
    context = {}
    return render(request, 'poll/home.html', context)

def create_view(request):
    context = {}
    return render(request, 'poll/create.html', context)

def vote_view(request , pk):
    context = {}
    return render(request, 'poll/vote.html', context)

def result_view(request , pk):
    context = {}
    return render(request, 'poll/result.html', context)
    
