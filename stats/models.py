from django.db import models
from django.forms import ModelForm
import cmislib

from stats.utils import parseFolder

class Repo(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    doclib = models.CharField(max_length=250)
    dirtree = models.TextField(blank=True)
    
    def update_directory(self):
        '''
        Consider: Only get directory contents of a user selected
        subfolder in order to reduce the time to complete the request
        ?However, when we want data/stats, we want it for the entire
        repo, right? So maybe that's a bad idea.        
        ''' 
        
        #Initialize list if it does not already exist.  
        try: 
            self.directory == self.directory #@NoEffect
        except: 
            self.direcory = []
        
        '''
        This code should function in a way to update the repository directory 
        in the db periodically. That way the ajax function can fetch what its 
        available through out the process. 
        '''

        cclient = cmislib.CmisClient(self.url, self.username, self.password)
        cmisrepo = cclient.defaultRepository
        rootfolder = cmisrepo.getRootFolder()
        
        self.directory.append(parseFolder(rootfolder))
        self.dirtree = 'hi this worked.'
        self.save()
        
        return
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/stats/%i/" % self.id
    
class RepoForm(ModelForm):
    class Meta:
        model = Repo