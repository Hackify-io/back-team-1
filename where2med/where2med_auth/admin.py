from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.MedicalCenter)
admin.site.register(models.Patient)
admin.site.register(models.Admin)
admin.site.register(models.Service)
admin.site.register(models.MedicalNote)
admin.site.register(models.Rate)
admin.site.register(models.Status)
admin.site.register(models.TelephoneAppointment)
admin.site.register(models.PhysicalAppointment)
admin.site.register(models.MedicalCenterService)