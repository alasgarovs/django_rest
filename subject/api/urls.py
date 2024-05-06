from django.urls import path
from subject.api import views as api_view

urlpatterns = [
    path('subjects/', api_view.SubjectListCreateAPIView.as_view(), name='subjects_list'),
    path('subjects/<int:pk>/', api_view.SubjectDetailAPIView.as_view(), name='subject_detail'),

]
