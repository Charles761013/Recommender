from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    
    owner = models.ForeignKey(User, related_name='own_user', verbose_name='Owner', null=True)
    review = models.CharField(max_length=512, null=True)
    history = models.CharField(max_length=128, null=True)
     
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.owner.username
