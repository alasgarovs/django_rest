from rest_framework import serializers
from subject.models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('The title len must be greater than 10 characters...')
        return value
