from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

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
        'PlanOfAccounts',
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

class Reports(models.Model):
    condominium = models.ForeignKey(
        Condominium,
        on_delete=models.CASCADE,
        related_name='reports',
    )

    @property
    def total_balance(self):
        receipts = self.condominium.receipts.all().aggregate(models.Sum('value'))
        expenses = self.condominium.expenses.all().aggregate(models.Sum('value'))
        return receipts - expenses

    @property
    def last_moonth_balance(self):
        today = datetime.date.today()
        receipts = self.condominium.receipts.all().filter(
            date__month=today.month,
            date__year=today.year,
        ).aggregate(models.Sum('value'))
        expenses = self.condominium.expenses.all().filter(
            date__month=today.month,
            date__year=today.year,
        ).aggregate(models.Sum('value'))
        return receipts - expenses

    class Meta:
        abstract = True