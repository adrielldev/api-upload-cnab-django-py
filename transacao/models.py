from django.db import models
import uuid


class Transacao(models.Model):

    

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    date = models.DateField()
    value = models.PositiveIntegerField()
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    time = models.TimeField()
    owner = models.TextField(max_length=14)
    store = models.TextField(max_length=19)
    

