from django.db import models
import uuid
from .property import Propertree
from django.forms import ModelForm
class ticket(models.Model):
    property_name = models.ForeignKey(Propertree,on_delete=models.PROTECT)
    ticket_id = models.UUIDField(primary_key=True,default = uuid.uuid4,editable = False)
    description = models.TextField()

    def __str__(self):
        return f"{self.property_name} {self.description[:10]}... "

class ticketForm(ModelForm):
    class Meta:
        model = ticket
        fields = '__all__'