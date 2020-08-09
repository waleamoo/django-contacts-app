from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    info = models.CharField(max_length=30,blank=True)
    gender = models.CharField(max_length=50, choices=(
        ('male', 'Male'),
        ('female', 'Female')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    data_added = models.DateTimeField(default=datetime.now)

#show name of the object instead of contactObject(1)...and so on in the admin side 
    def __str__(self):
        return self.name
    # order the contact in desc order of id column 
    class Meta:
        ordering = ['-id']
    