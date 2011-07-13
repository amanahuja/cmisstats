from stats.models import Repo, RepoForm
from django.template import RequestContext
from django.shortcuts import render_to_response

def list (request):
    repos = Repo.objects.all()
    return render_to_response('list.html', {
        'repo_list': repos,
        }) 
        
def addRepo (request):    
    if request.method == 'POST': 
        form = RepoForm(request.POST)
        if form.is_valid():
            form.save
            
    else:  
        form = RepoForm()
        
    return render_to_response("addrepo.html", {
        "form": form, 
        }, context_instance=RequestContext(request))