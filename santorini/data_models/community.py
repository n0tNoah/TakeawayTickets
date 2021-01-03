from django.db import models
import uuid
class community(models.Model):
    name = models.CharField(max_length=300)
    community_id =models.UUIDField(primary_key=True,default = uuid.uuid4,editable = False)

    def __str__(self):
        return self.name
