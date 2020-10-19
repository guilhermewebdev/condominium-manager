from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class PlanOfAccounts(models.Model):
    name = models.CharField(
        max_length=150,
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

class Expense(models.Model):
    plan_of_account = models.ForeignKey(
        PlanOfAccounts,
        on_delete=models.DO_NOTHING,
        related_name='expenses'
    )
    value = models.IntegerField(
        verbose_name='Value',
        validators=[
            MinValueValidator(0),
        ]
    )
    date = models.DateTimeField(
        verbose_name='Date',
    )

class Receiving(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.DO_NOTHING,
        related_name='receipts',
    )
    value = models.IntegerField(
        verbose_name='Value',
        validators=[
            MinValueValidator(0),
        ]
    )
    date = models.DateTimeField(
        verbose_name='Date',
    )