from django.db import models

# Create your models here.
#fajl u kome pisemo svoje modele
#definisemo promjenjivu i koji je tip podatka ovo name i CharField


class Dog(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    
    def __str__(self):
       return self.name +', '+ str(self.age)

class Cat(models.Model):
    name= models.CharField(max_length=250)
    age= models.IntegerField()

    def __str__(self):
        return self.name + ', '+ str(self.age)

