# Generated by Django 3.2.5 on 2021-07-24 06:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Material_Code', models.CharField(blank=True, max_length=255, null=True)),
                ('Material_Descriptions', models.CharField(blank=True, max_length=255, null=True)),
                ('Material_Location', models.CharField(blank=True, max_length=255, null=True)),
                ('Unit_of_Measurement', models.CharField(blank=True, default=0, max_length=255, null=True)),
                ('Maximum_Level', models.IntegerField(blank=True, default=0, null=True)),
                ('Minimum_Level', models.IntegerField(blank=True, default=0, null=True)),
                ('Re_order_Level', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
