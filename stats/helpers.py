from django.shortcuts import get_object_or_404
from django.http import Http404
import cmislib
from stats.models import Repo

def CMISRepoConnector(user, repo_id = 1):
    '''
    Establishes a connection to the specified repo
    Args: 
        repo_id = primary key for Repo in Django db. Uses '1' for CGDocMgmnt repo by default
        user = User object model from Django user db. 
    todo:
        Error catching with useful returns
    '''
    cmisrepo = get_object_or_404(Repo, pk=repo_id)

    #Attempt to connect to repository    
    try: 
        cclient = cmislib.CmisClient(cmisrepo.url, cmisrepo.username, cmisrepo.password)
        crepo = cclient.defaultRepository
    except Exception:
        raise Http404('\nError in utils.CMISRepoConnector(): Unable to connect to repository.')

    return crepo