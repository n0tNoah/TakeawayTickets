from django.db import models
import uuid
from .community import community
class Propertree(models.Model):
    name = models.CharField(max_length=300)
    property_manager = models.CharField(max_length=300)
    property_id =models.UUIDField(primary_key=True,default = uuid.uuid4,editable = False)
    parent_community = models.ForeignKey(community,on_delete=models.PROTECT)
    default_assignee = models.CharField(max_length=300,blank=True,null=True)
    
    def __str__(self):
        return self.name