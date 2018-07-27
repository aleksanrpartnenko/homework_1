from rest_framework import serializers
from .models import ENTRY

class ENTRYSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ENTRY
        fields = ( 'id', 'NAME', 'PLATE', )