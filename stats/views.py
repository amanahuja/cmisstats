from stats.models import RepoForm
from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request):
    
    if request.method == 'POST': 
        form = RepoForm(request.POST)
        if form.is_valid():
            form.save
            
    else:  
        form = RepoForm()
        
    return render_to_response("test.html", {
        "form": form, 
        }, context_instance=RequestContext(request))