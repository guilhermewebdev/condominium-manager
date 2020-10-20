# Generated by Django 3.1.2 on 2020-10-20 00:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('apartament', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Condominium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Receiving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Value')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='receipts', to='core.client')),
                ('condominium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipts', to='core.condominium')),
            ],
        ),
        migrations.CreateModel(
            name='PlanOfAccounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('due_date', models.IntegerField(validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MaxValueValidator(1)], verbose_name='Due Date')),
                ('condominium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_of_accounts', to='core.condominium')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='core.planofaccounts')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Value')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('condominium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='core.condominium')),
                ('plan_of_account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='expenses', to='core.planofaccounts')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='condominium',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='core.condominium'),
        ),
    ]