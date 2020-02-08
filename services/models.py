from django.db import models


# Create your models here.
class services(models.Model):
    name = models.CharField(max_length=150)
    describe = models.TextField()
    img  =     models.ImageField(upload_to='photos', blank=True)
    
    
    


    def __str__(self):
        return self.name
    

    
