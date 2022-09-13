
from django.urls import path
from . import views
from .views import ApplicantDeleteAPIView, ApplicantGetAPIView, ApplicantGetAllAPIView, ApplicantPostAPIView, ApplicantPutAPIView, ResultPostAPIView



urlpatterns = [
    path('index/', views.index, name='index'),
    path('applicant/list/', ApplicantGetAllAPIView.as_view(), name='list_applicants'),
    path('applicant/get/<str:status_field>/' ,ApplicantGetAPIView.as_view(), name='get_applicant'),
    path('applicant/post/', ApplicantPostAPIView.as_view(), name='post_applicant'),
    path('applicant/delete/<int:id_applicant>/', ApplicantDeleteAPIView.as_view(), name='delete_applicant'),
    path('applicant/put/<int:id_applicant>/', ApplicantPutAPIView.as_view(), name='put_applicant'),

    path('process/<int:id>/', ResultPostAPIView.as_view(), name="post_result"),
]
