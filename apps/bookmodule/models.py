from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)


class Address(models.Model):
    city = models.CharField(max_length=100)
    def __str__(self):
        return self.city
    
class Student(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    address =models.ForeignKey(Address, on_delete=models.CASCADE)


class Address2(models.Model):
    city = models.CharField(max_length=100)
    def __str__(self):
        return self.city
    
class Student3(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    address =models.ManyToManyField(Address2)

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



class Author(models.Model):
    fullname=models.CharField(max_length=100, null=False)
    address = models.TextField(max_length=500, null=True)
    def __str__(self): 
        return self.fullname
    
class Book2(models.Model):
    title = models.CharField(max_length=100, null= False)
    price = models.FloatField(default=0)
    authors = models.ManyToManyField(Author)  
    coverPage = models.FileField(upload_to='documents/', blank=True, null=True)
    def __str__(self):
        return self.title

