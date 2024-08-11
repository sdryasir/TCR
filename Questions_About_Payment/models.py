from django.db import models

# Create your models here.
class Payment_Questions(models.Model):
    Question = models.CharField(max_length=200,null=True)
    Answer = models.CharField(max_length=700,null=True)



    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Payment Questions"  # Plural name (same as singular, to avoid pluralization)