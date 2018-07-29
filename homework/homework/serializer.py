from rest_framework import serializers
from .models import ENTRY

class ENTRYSerializer(serializers.ModelSerializer):
    class Meta:
        model = ENTRY
        fields = ( 'id', 'NAME', 'PLATE', )