# Generated by Django 2.2.3 on 2019-07-25 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('departamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do funcionário', max_length=100)),
                ('departamentos', models.ManyToManyField(to='departamentos.Departamento')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empresas.Empresa')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
