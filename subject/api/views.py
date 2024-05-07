from subject.api.serializers import SubjectSerializer, CommentSerializer
from rest_framework import generics

from subject.models import Subject, Comment

class SubjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    

class SubjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        subject_pk = self.kwargs.get('subject_pk')
        subject = generics.get_object_or_404(Subject, pk=subject_pk)
        serializer.save(subject=subject)

class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
