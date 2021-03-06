# Generated by Django 2.1.3 on 2020-01-18 23:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(default=1)),
                ('producto', models.TextField(max_length=140)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('reposicion', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
