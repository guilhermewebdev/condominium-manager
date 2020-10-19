from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class PlanOfAccounts(models.Model):
    name = models.CharField(
        max_lengt=150,
    )
    due_date = models.IntegerField(
        verbose_name="Due Date",
        validators=[
            MaxValueValidator(31),
            MaxValueValidator(1)
        ]
    )
    parent = models.ForeignKey(
        PlanOfAccounts,
        on_delete=models.CASCADE,
        null=True,
        related_name='childs',
    )

class Client(models.Model):
    name = models.CharField(
        max_length=150,
    )
    apartament = models.CharField(
        max_length=5
    )

    