from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from subject.api.serializers import SubjectSerializer, CommentSerializer
from subject.models import Subject


class SubjectListCreateGenericAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
