from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    date = models.DateTimeField()
    category = models.CharField(max_length=110, blank=True, null=True)
    payment_method = models.CharField(max_length=50, choices=[
        ("Dinheiro", "Dinheiro"),
        ("Cartão de crédito", "Cartão de crédito"),
        ("Cartão de débito", "Cartão de débito")
    ])

    def __str__(self):
        return f"{self.description} - {self.amount}"
