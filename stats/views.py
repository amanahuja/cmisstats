from stats.models import Repo, RepoForm
from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request):
    repos = Repo.objects.all()
    return render_to_response('test.html', {
        'repo_list': repos,
        }) 
        

def addRepo (request):    
    if request.method == 'POST': 
        form = RepoForm(request.POST)
        if form.is_valid():
            form.save
            
    else:  
        form = RepoForm()
        
    return render_to_response("test.html", {
        "form": form, 
        }, context_instance=RequestContext(request))