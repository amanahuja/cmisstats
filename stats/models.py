from django.db import models
from django.forms import ModelForm

class Repo(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    doclib = models.CharField(max_length=250)
        
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/repo/%i/" % self.id
    
class RepoForm(ModelForm):
    class Meta:
        model = Repo