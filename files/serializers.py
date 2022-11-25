

from rest_framework import serializers
from .models import File
from pathlib import Path
import os
from transacao.models import Transacao

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
                dict_transacao = {
                    'type':line[:1],
                    'date':line[1:9],
                    'valor':line[9:20],
                    'cpf':line[20:31],
                    'cartao':line[31:42],
                    'time':line[42:48],
                    'owner':line[48:62],
                    'store':line[62:81]
                }


        return file

