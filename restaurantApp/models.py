from django.db import models

# Create your models here.
class Table1(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    date=models.DateField()
    time=models.TimeField()
    people=models.IntegerField()
    message=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name



class Contact2(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.TextField(max_length=100)
    message=models.TextField(max_length=600)

    def __str__(self):
        return  self.name
class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
