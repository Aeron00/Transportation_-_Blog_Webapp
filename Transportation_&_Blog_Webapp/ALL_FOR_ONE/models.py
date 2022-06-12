from django.db import models
from datetime import date

# Create your models here.

# class admin_login(models.Model):
#     admin = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)

class SignUp(models.Model):
    Pro_Img = models.FileField(upload_to='Profile/')
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Password = models.CharField(max_length=50)
    Phone = models.IntegerField()
    Address = models.CharField(max_length=200)
    Date = models.DateField(default=date.today)

    def __str__(self):
        return self.Name


class Blog(models.Model):
    U_id = models.ForeignKey(SignUp, on_delete=models.CASCADE)
    File = models.FileField(upload_to='Blog/')
    Title = models.CharField(max_length=30)
    Detail = models.CharField(max_length=10000)
    Date = models.DateField(default=date.today)
    U_Name = models.CharField(max_length=50)

    def __str__(self):
        return self.U_Name


class Comments(models.Model):
    U_id = models.ForeignKey(SignUp, on_delete=models.CASCADE)
    Blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    Date = models.DateField(default=date.today)

    def __str__(self):
        return self.comment


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField()
    phone = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.name