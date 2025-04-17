from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)


class Address(models.Model):
    city = models.CharField(max_length=100)
    
class Student(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    address =models.ForeignKey(Address, on_delete=models.CASCADE)

class department(models.Model):
    name = models.CharField(max_length = 50)
    
class card(models.Model):    
    card_number = models.SmallIntegerField(default = 1)

class course(models.Model):   
    title = models.CharField(max_length = 50)
    code = models.SmallIntegerField(default = 1)
    
class student2(models.Model):
  name = models.CharField(max_length = 50)
  card = models.OneToOneField(card, on_delete=models.PROTECT)
  department = models.ForeignKey(department, on_delete=models.CASCADE)
  course = models.ManyToManyField(course)