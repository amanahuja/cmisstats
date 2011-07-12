from stats.models import RepoForm
from django.shortcuts import render_to_response

def home(request):
    form = RepoForm()
    
    return render_to_response("test.html", {
        "form": form, 
        })