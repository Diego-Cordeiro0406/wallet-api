from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)


class Login(models.Model):
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
