from django.db import models
from django.utils.timezone import now

from django.contrib.auth.models import User

def get_image_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("images", filename)

# Create your models here.
class MedicalCenter(models.Model):
    name = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    phone = models.CharField(max_length=10)
    # image = models.ImageField(
    #     upload_to=get_image_file_path,
    #     height_field="image_heigth",
    #     width_field="image_width",
    # )
    #image_heigth = models.IntegerField(default=0, editable=False)
    #image_width = models.IntegerField(default=0, editable=False)
    cost_per_consult = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.FloatField(default=0.0)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    phone = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    # image = models.ImageField(
    #    upload_to=get_image_file_path,
    #    height_field="image_heigth",
    #    width_field="image_width",
    # )
    # image_heigth = models.IntegerField(default=0, editable=False)
    # image_width = models.IntegerField(default=0, editable=False)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    medical_center = models.ForeignKey(MedicalCenter, on_delete=models.CASCADE)
    # image = models.ImageField(
    #     upload_to=get_image_file_path,
    #     height_field="image_heigth",
    #     width_field="image_width",
    # )
    # image_heigth = models.IntegerField(default=0, editable=False)
    # image_width = models.IntegerField(default=0, editable=False)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

class Service(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

class MedicalNote(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medical_center = models.ForeignKey(MedicalCenter, on_delete=models.CASCADE)
    note = models.TextField(max_length=1024)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

class Rate(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medical_center = models.ForeignKey(MedicalCenter, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        unique_together = (("patient", "medical_center"),)

class Status(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

class TelephoneAppointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medical_center = models.ForeignKey(MedicalCenter, on_delete=models.CASCADE)
    appointment_at = models.DateTimeField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

class PhysicalAppointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medical_center = models.ForeignKey(MedicalCenter, on_delete=models.CASCADE)
    appointment_at = models.DateTimeField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

class MedicalCenterService(models.Model):
    medical_center = models.ForeignKey(MedicalCenter, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("medical_center", "service"),)

