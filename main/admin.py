from django.contrib import admin
from .models import ResultProfile
from .models import AdmissionEnquiry

# Register your models here.
admin.site.register(ResultProfile)
admin.site.register(AdmissionEnquiry)