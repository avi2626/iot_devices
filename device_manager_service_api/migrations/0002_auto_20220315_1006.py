# Generated by Django 2.2.8 on 2022-03-15 07:11

from django.db import migrations


def seed_data(apps, schema_editor):

    Person = apps.get_model('device_manager_service_api', 'Airplane')
    objs = Person.objects.bulk_create([
        Person(id='no_airplane'),
        Person(id='airplane1'),
        Person(id='airplane2'),
        Person(id='airplane3'),
        Person(id='airplane4'),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('device_manager_service_api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data),
    ]