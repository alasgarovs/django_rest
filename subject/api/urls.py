from django.urls import path
from subject.api import views as api_view

urlpatterns = [
    path('subjects/', api_view.SubjectListCreateAPIView.as_view(), name='subjects_list'),
    path('subjects/<int:pk>', api_view.SubjectDetailAPIView.as_view(), name='subject_detail'),
    path('subjects/<int:subject_pk>/add_comment', api_view.CommentCreateAPIView.as_view(), name='add_comment'),
    path('comments/<int:pk>', api_view.CommentDetailAPIView.as_view(), name='comment_detail'),
]
