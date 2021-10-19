from django.db import models

# Create your models

class Contactus(models.Model):
    
    email=models.EmailField(max_length=100)
    query=models.CharField(max_length=200)
    suggestion=models.CharField(max_length=200)

    def __str__ (self):
        return self.email