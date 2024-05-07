from rest_framework import generics
from rest_framework import permissions
from rest_framework.exceptions import ValidationError

from subject.api.permissions import IsAdminUserOrReadOnly, IsCommenterOrReadOnly
from subject.api.pagination import LargePagination
from subject.api.serializers import SubjectSerializer, CommentSerializer
from subject.models import Subject, Comment

class SubjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = LargePagination
    

class SubjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        subject_pk = self.kwargs.get('subject_pk')
        subject = generics.get_object_or_404(Subject, pk=subject_pk)
        user = self.request.user
        comments = Comment.objects.filter(subject=subject, commenter=user)
        if comments:
            raise ValidationError('User only add one comment to one book')
        serializer.save(subject=subject, commenter=user)

class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommenterOrReadOnly]
