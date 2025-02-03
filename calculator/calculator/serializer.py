from rest_framework import serializers
from .models import Ans
class AnsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Ans
        fields= ['answer']
