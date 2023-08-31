from django.db import models

class EventRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    dob = models.DateField()
    signature = models.CharField(max_length=255)
    inspiration = models.TextField(max_length=5000)
    art_works = models.FileField(null=True)

    def __str__(self):
        return self.name

