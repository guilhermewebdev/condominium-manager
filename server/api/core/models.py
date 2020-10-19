from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Condominium(models.Model):
    name = models.CharField(
        max_length=150
    )
class PlanOfAccounts(models.Model):
    condominium = models.ForeignKey(
        Condominium,
        on_delete=models.CASCADE,
        related_name='plan_of_accounts',
    )
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
    condominium = models.ForeignKey(
        Condominium,
        on_delete=models.CASCADE,
        related_name='clients',
    )
    name = models.CharField(
        max_length=150,
    )
    apartament = models.CharField(
        max_length=5
    )

class Expense(models.Model):
    condominium = models.ForeignKey(
        Condominium,
        on_delete=models.CASCADE,
        related_name='expenses',
    )
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
    condominium = models.ForeignKey(
        Condominium,
        on_delete=models.CASCADE,
        related_name='receipts',
    )
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
