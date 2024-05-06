from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from subject.api.serializers import SubjectSerializer
from subject.models import Subject


class SubjectListCreateAPIView(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class SubjectDetailAPIView(APIView):

    def get_object(self, pk):
        subject_instance = get_object_or_404(Subject, pk=pk)
        return subject_instance

    def get(self, request, pk):
        subject = self.get_object(pk)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    def put(self, request, pk):
        subject = self.get_object(pk)
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        subject = self.get_object(pk)
        subject.delete()
        return Response(status.HTTP_204_NO_CONTENT)
