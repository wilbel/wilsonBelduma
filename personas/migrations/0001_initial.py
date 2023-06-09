# Generated by Django 4.1.7 on 2023-03-28 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pais', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(unique=True)),
                ('nombre', models.CharField(blank=True, max_length=50)),
                ('nacimiento', models.DateField()),
                ('nacionalidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pais.pais')),
            ],
        ),
    ]
