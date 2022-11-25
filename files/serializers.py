

from rest_framework import serializers
from .models import File
from pathlib import Path
import os
from transacao.models import Transacao
from datetime import date

class FileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=False)
    class Meta:
        model = File
        fields = '__all__'
    
    def create(self,validated_data:dict):
        file = File.objects.create(**validated_data)
        filename = file.file.name[6:]
        with open(f"{os.path.join(os.path.dirname(Path(__file__).resolve().parent.parent), 'mediafiles')}/texts/{filename}",'r',encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
               
                data_transaction = date(int(line[1:5]),int(line[5:7]),int(line[7:9])).isoformat()
                time_transaction = f'{line[42:44]}:{line[44:46]}:{line[46:48]}'

                dict_transacao = {
                    'type':line[:1],
                    'date':data_transaction,
                    'value':line[9:20],
                    'cpf':line[20:31],
                    'card':line[31:42],
                    'time':time_transaction,
                    'owner':line[48:62],
                    'store':line[62:81]
                }
                Transacao.objects.create(**dict_transacao)


        return file

