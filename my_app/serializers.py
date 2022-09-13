from rest_framework import serializers
from .models import Applicants, Results


class ApplicantGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicants
        fields = ('applicant_id','name','email','dob','country', 'status','created_dttm')

class ApplicantPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicants
        fields = ('name','email','dob','country',)