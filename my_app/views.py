from ast import Delete
from email.policy import default
from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,filters
from .models import Applicants,Results
from .serializers import ApplicantGetSerializer, ApplicantPostSerializer
from my_app import serializers
from rest_framework.parsers import JSONParser
# Create your views here.

def index(request):
    return HttpResponse("Hello world!")

class ApplicantGetAllAPIView(APIView):
    def get(self,request):
        all_data_get = Applicants.objects.all()
        if not all_data_get:
            return Response(data='Can not get all data in db', status=status.HTTP_404_NOT_FOUND)
        else:
            Serializer_all_data_get = ApplicantGetSerializer(all_data_get, many=True)
            return Response(data=Serializer_all_data_get.data, status=status.HTTP_200_OK)


class ApplicantGetAPIView(APIView):
    def get(self,request,status_field):
        data_get = Applicants.objects.filter(status = status_field)
        if not data_get:
            return Response(data="Can not get data", status=status.HTTP_400_BAD_REQUEST)
        else:
            Serializer_data_get = ApplicantGetSerializer(data_get, many= True)
            return Response(Serializer_data_get.data, status=status.HTTP_200_OK)
    
class ApplicantPostAPIView(APIView):
    def post(self, request):
        data_post = request.data
        Serializer_data_post = ApplicantPostSerializer(data = data_post)
        if Serializer_data_post.is_valid():
            post_name = Serializer_data_post.data['name']
            post_email = Serializer_data_post.data['email']
            post_dob = Serializer_data_post.data['dob']
            post_country = Serializer_data_post.data['country']
            Applicants.objects.create(name = post_name, email = post_email, dob = post_dob, country= post_country)
            return Response(data="oke", status=status.HTTP_200_OK)
        else:
            return Response(data='data request is not valid', status=status.HTTP_400_BAD_REQUEST)

class ApplicantDeleteAPIView(APIView):
    def delete(self,request,id_applicant):
        data_delete = Applicants.objects.get(applicant_id = id_applicant)
        data_delete.delete()
        return Response(data="Deleted", status=status.HTTP_200_OK)

# bug
# '127.0.0.1:8000/applicant/put/<int:id_applicant>/'
class ApplicantPutAPIView(APIView):
    def put(self,request,id_applicant):
        try:
            data_get = Applicants.objects.get(applicant_id = id_applicant)
        except Applicants.DoesNotExist:
            return Response(data='can not get data',status=status.HTTP_404_NOT_FOUND)
        request_data = request.data 
        serializer_request_data = ApplicantGetSerializer(data_get,data=request_data)
        if serializer_request_data.is_valid():
            serializer_request_data.save()
            return Response(data=serializer_request_data.data ,status=status.HTTP_200_OK)
        return Response(data=serializer_request_data.errors, status=status.HTTP_400_BAD_REQUEST)


class ResultPostAPIView(APIView):
    def post(self,request,id):
        data_get_from_Applicant = Applicants.objects.get(applicant_id = id)
        # print(type(data_get_from_Applicant.dob.strftime("%d")))
        if int(data_get_from_Applicant.dob.strftime("%d")) % 2 == 0:
            status_process = "processed"
        else:
            status_process = "failed"
        Results.objects.create(applicant_id = id,applicant_status = status_process)
        data_get_from_Applicant.status = status_process
        data_get_from_Applicant.save()
        return Response(status=status.HTTP_200_OK)




