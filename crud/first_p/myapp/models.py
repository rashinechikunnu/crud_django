from django.db import models

# Create your models here.

class actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=2)
    place = models.CharField(max_length=100)
    email=models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.TextField(null=True)
    course_choices =[
        ('BCA','BCA'),
        ('BBA','BBA'),
        ('MBA','MBA'),
        ('MCA','MCA'),
    ]

    course = models.CharField(null=True,max_length=10,choices=course_choices)
                     
 
    gender = models.CharField(null=True,max_length=10)
    image = models.ImageField(upload_to="media/")


    def __str__(self):
        return self.name
    
