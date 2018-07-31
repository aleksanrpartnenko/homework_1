from rest_framework import serializers
from .models import ENTRY
import re

class ENTRYSerializer(serializers.ModelSerializer):
    class Meta:
        model = ENTRY
        fields = ( 'id', 'NAME', 'PLATE', )
    def validate_PLATE(self, value):
        pattern = re.compile("[a-zA-z]{3}[\d]{3}$")
        if not pattern.match(value.lower()):
            raise serializers.ValidationError("PLATE is wrong")
        return value
    def validate_NAME(self, value):
        pattern = re.compile("[a-zA-z]{1,20} [a-zA-z]{1,20}$")
        if not pattern.match(value.lower()):
            raise serializers.ValidationError("NAME is wrong")
        return value