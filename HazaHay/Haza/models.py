from djongo import models

# Create your models here.


class User(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    matricule = models.CharField(max_length=20,primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

def __str__(self):
    return self.matricule