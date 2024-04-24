# Generated by Django 4.2.11 on 2024-04-16 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('keshoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_number', models.IntegerField(blank=True, max_length=5, null=True)),
                ('amount', models.IntegerField(blank=True, max_length=10, null=True)),
                ('currency', models.CharField(blank=True, default='Ugx', max_length=5, null=True)),
                ('c_payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='keshoApp.categorystay')),
            ],
        ),
        migrations.AddField(
            model_name='babe',
            name='c_fee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='keshoApp.payment'),
        ),
    ]