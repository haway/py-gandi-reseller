from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    user = models.ForeignKey(
                User,
                related_name='contacts',
                on_delete = models.CASCADE
            )
    given = models.CharField(max_length=20)
    family = models.CharField(max_length=20)
    email = models.EmailField()
    ctid = models.CharField(max_length=20)
    enaddr = models.CharField(max_length=150)
    zhaddr = models.CharField(max_length=150)
    zip = models.CharField(max_length=20)
    countrycode = models.CharField(max_length=2)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    fax = models.CharField(max_length=20)
    type = models.IntegerField()

