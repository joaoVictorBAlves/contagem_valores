# Generated by Django 3.2.8 on 2024-12-30 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtualizacaoGlobal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_atualizacoes', models.IntegerField(default=0)),
            ],
        ),
    ]
