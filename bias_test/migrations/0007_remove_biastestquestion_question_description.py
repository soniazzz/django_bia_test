# Generated by Django 4.2.1 on 2023-05-23 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bias_test', '0006_alter_biastestquestion_question_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biastestquestion',
            name='question_description',
        ),
    ]
