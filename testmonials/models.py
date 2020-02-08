from django.db import models
import datetime

# Create your models here.
class testimonies(models.Model):
    name = models.CharField(max_length=150)
    titleID = models.CharField(max_length=150)
    testmony= models.TextField()
    img =models.ImageField(upload_to='photos', blank=True, default='photos/defpic.jpg')
    datepost=models.DateField(blank=True,auto_now_add=True)
    
    


    def __str__(self):
        return self.name  + " " + self.titleID
    

    
