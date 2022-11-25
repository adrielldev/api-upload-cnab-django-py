from django.db import models

import uuid

def upload_to(instance,filename):
    return 'texts/{filename}'.format(filename=filename)

class File(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    file = models.FileField(upload_to=upload_to,blank=True,null=True)

    


