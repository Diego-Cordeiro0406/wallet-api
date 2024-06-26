from rest_framework import serializers
from .models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            "id",
            "user",
            "amount",
            "description",
            "date",
            "category",
            "payment_method"
        ]
        read_only_fields = ['id', 'user']
