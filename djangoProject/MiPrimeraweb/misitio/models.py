from django.db import models

# Create your models here.

class contacto(models.Model):
    Email = models.EmailField()
    Subject = models.CharField(max_length=196)
    Message = models.TextField()

    def __str__(self):
         return self.Email

    # def __unicode__(self):
    #     return 
