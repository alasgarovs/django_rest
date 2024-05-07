from django.urls import path
from subject.api import views as api_view

urlpatterns = [
    path('subjects/', api_view.SubjectListCreateGenericAPIView.as_view(), name='subjects_list'),

]
