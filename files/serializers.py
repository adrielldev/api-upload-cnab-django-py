

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
                    
                }
                print(line[:1]) # tipo de transação
                print(line[1:9]) # data ocorrencia
                print(line[9:20]) # valor 
                print(line[20:31]) # cpf
                print(line[31:42]) # cartao
                print(line[42:48]) # hora
                print(line[48:62]) # dono da loja
                print(line[62:81]) # nome da loja

        return file

