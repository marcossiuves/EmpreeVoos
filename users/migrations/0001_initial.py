# Generated by Django 2.2.24 on 2021-11-29 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modify_date', models.DateField(auto_now=True, verbose_name='Data de Atualização')),
                ('verified_user', models.BooleanField(default=True, verbose_name='Verificado')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ('name',),
            },
        ),
    ]
