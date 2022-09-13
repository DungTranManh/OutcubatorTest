import imp
from django.contrib import admin
from django.db import models 
from .models import Applicants, Results
from django.forms import Textarea
# Register your models here.

class ApplicantsAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': Textarea(
                       attrs={'rows': 2,
                              'cols': 10})},
    }
    list_display = ('applicant_id', 'name','email','dob','country', 'status','created_dttm',)
    list_editable = ('name','email','dob','country', 'status','created_dttm',)
admin.site.register(Applicants,ApplicantsAdmin)


class ResultsAdmin(admin.ModelAdmin):
    list_display = ('applicant_id','client_key','applicant_status','processed_dttm')
admin.site.register(Results,ResultsAdmin)



