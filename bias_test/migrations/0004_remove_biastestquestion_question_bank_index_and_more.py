# Generated by Django 4.2.1 on 2023-05-21 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bias_test', '0003_biastestquestion_question_bank_index_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biastestquestion',
            name='question_bank_index',
        ),
        migrations.RemoveField(
            model_name='biastestquestion',
            name='question_description',
        ),
    ]
