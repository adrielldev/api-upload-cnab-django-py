from django.db import models
import uuid


class Transacao(models.Model):

    choices_type = [
        (1,'Debito'),
        (2,'Boleto'),
        (3,'Financiamento'),
        (4,'Credito'),
        (5,'Recebimento Emprestimo'),
        (6,'Vendas'),
        (7,'Recebimento TED'),
        (8,'Recebimento DOC'),
        (9,'Aluguel'),

        
    ]

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.CharField(max_length=1,chocies=choices_type)
    date = models.DateField()
    value = models.PositiveIntegerField()
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    time = models.TimeField()
    owner = models.TextField(max_length=14)
    store = models.TextField(max_length=19)
    

