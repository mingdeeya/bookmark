from .models import *
from rest_framework import serializers

class QuestionSerializer(serializers.Modelserializer):
    class Meta:
        model = Bookmark
        fields = '__all__'