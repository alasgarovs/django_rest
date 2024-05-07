from rest_framework import serializers
from subject.models import Subject, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['subject']


class SubjectSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Subject
        fields = '__all__'

