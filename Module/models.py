from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Doctor(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    specialization = models.CharField(max_length=255,null=True)
    experience = models.IntegerField()
    password = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    username=models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    patient = models.CharField(max_length=100)
    num_days = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.doctor.name} - {self.appointment_time}"

    class User(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField(unique=True)
        phone = models.CharField(max_length=20)
        address = models.CharField(max_length=255)
        age = models.PositiveIntegerField()
        height = models.FloatField()  # Assuming height is in centimeters
        weight = models.FloatField()  # Assuming weight is in kilograms

        # Add any other fields you need
        class Meta:
            db_table: "User"

