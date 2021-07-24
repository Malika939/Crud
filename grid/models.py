from django.db import models

class Employer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    contact = models.CharField(max_length=100)

    class Meta:
        db_table = 'employer'

