from stats.models import Repo, RepoForm
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404 
from django.http import HttpResponse

from stats.helpers import CMISRepoConnector, parseFolder

def list (request):
    repos = Repo.objects.all()
    return render_to_response('list.html', {
        'repo_list': repos,
        }) 
        
def addRepo (request):    
    if request.method == 'POST': 
        form = RepoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Added repository'.format(form.cleaned_data.items()))
            
    else:  
        form = RepoForm()
        
    return render_to_response("addrepo.html", {
        "form": form, 
        }, context_instance=RequestContext(request))

def info(request, repo_id):
    cmisserver = get_object_or_404(Repo, pk=repo_id)
    cmisrepo = CMISRepoConnector(repo_id)
    
    '''
    The following is hard coded and should not be. For testing only. 
    todo: autodetect these paths
    '''
    #/sites/capgemini/documentLibrary/
    site = cmisrepo.getObjectByPath(cmisserver.doclib)
    properties = site.getProperties
    return render_to_response('info.html', {
        'site':site, 
        'properties':properties,
        'repo_name':cmisserver.name,
        'repo_url':cmisserver.url,
        }, context_instance=RequestContext(request))

def browse(request, repo_id):
    
    '''
    
    ''' 
    # todo: We've already connected here and should use a persisted connection.
    '''
    cmisserver = get_object_or_404(Repo, pk=repo_id)
    cmisrepo = CMISRepoConnector(repo_id)
    
    rootfolder = cmisrepo.getRootFolder()
    directory = [] 
    directory.append(parseFolder(rootfolder))
    '''
     
    return render_to_response('browse.html', {
            'rootfolder': "rootfolder.name",
            'directory': "directory",
            })

def ajax_directory_tree( request ):
    if request.is_ajax():
        results = Repo.objects.all()
    else:
        return HttpResponse('not an AJAX request.')
        
    return render_to_response( 'json_template_handler.html', 
       {'results': results,},
       context_instance = RequestContext( request ) )