# Generated by Django 5.0.6 on 2024-06-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPMagic', '0002_contacto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profesor',
            old_name='FIELDNAME',
            new_name='Cursos',
        ),
        migrations.AlterField(
            model_name='grupos',
            name='nombre',
            field=models.CharField(choices=[('Aprendices de las Estrellas', '1 año : Aprendices de las Estrellas'), ('Exploradores de los Encantos', '2 año : Exploradores de los Encantos'), ('Guardianes de las Criaturas', '3 año :Guardianes de las Criaturas'), ('Alquimistas del Bosque', '4 año : Alquimistas del Bosque'), ('Maestros de la Magia', '5 año :Maestros de la Magia')], max_length=30, unique=True),
        ),
    ]
