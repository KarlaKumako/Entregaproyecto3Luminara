# Generated by Django 5.0.6 on 2024-06-03 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APPMagic', '0003_rename_fieldname_profesor_cursos_alter_grupos_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='FIELDNAME',
            new_name='Grupos',
        ),
    ]