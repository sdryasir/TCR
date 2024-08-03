from django.db import models
class Contact(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    messagesubject = models.CharField(max_length=60)
    message = models.TextField()
