from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='cars')
    specs = models.FileField(upload_to='specs')


class User(models.Model):
    avatar = models.ImageField(upload_to='avatars/')
    name = models.CharField(max_length=75)
