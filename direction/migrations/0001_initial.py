# Generated by Django 2.2 on 2020-07-29 01:20

import direction.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('nivel', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('horario', models.CharField(max_length=50)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direction.Grado')),
            ],
        ),
        migrations.CreateModel(
            name='PadreTutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autorizado', models.BooleanField(default=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='static/padres_tutores')),
                ('nombre_completo', models.TextField(verbose_name='Nombre Completo')),
                ('edad', models.IntegerField(default='', verbose_name='Edad')),
                ('folio', models.CharField(max_length=40, verbose_name='Folio')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=300)),
                ('location', models.TextField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='static/images')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(choices=[('direccion', 'Dirección'), ('profesor', 'Profesor')], max_length=100)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='static/profs')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direction.Grupo')),
                ('useras', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apaterno', models.CharField(max_length=200, verbose_name='A. Paterno')),
                ('amaterno', models.CharField(default='', max_length=200, verbose_name='A. Materno')),
                ('nombre', models.CharField(default='', max_length=200, verbose_name='Nombre')),
                ('curp', models.CharField(max_length=200, unique=True, verbose_name='CURP')),
                ('nacimiento', models.DateField(verbose_name='Fecha Nacimiento')),
                ('genero', models.CharField(choices=[('masculino', 'Masculino'), ('femenino', 'Femenino')], max_length=10, verbose_name='Genero')),
                ('lugar_nacimeinto', models.CharField(max_length=500, verbose_name='Lugar nacimeinto')),
                ('domicilio', models.TextField(verbose_name='Domicilio')),
                ('peso', models.CharField(max_length=10, verbose_name='Peso')),
                ('medida', models.CharField(max_length=10, verbose_name='Peso')),
                ('tipo_desangre', models.CharField(max_length=10, verbose_name='Tipo Sangre')),
                ('otra_escuela', models.TextField(blank=True, null=True)),
                ('peso_al_nacer', models.CharField(blank=True, max_length=10, null=True, verbose_name='Peso al nacer')),
                ('talla_al_nacer', models.CharField(blank=True, max_length=10, null=True, verbose_name='Medida al nacer')),
                ('enfermedad_cronica', models.CharField(blank=True, max_length=500, null=True, verbose_name='Enfermedad Crónica')),
                ('alergias', models.TextField(blank=True, null=True, verbose_name='Alergias')),
                ('goples', models.TextField(blank=True, null=True, verbose_name='Golpes en la cabeza')),
                ('alimentacion', models.TextField(blank=True, null=True, verbose_name='Alimentación')),
                ('esfinteres', models.CharField(choices=[('dia', 'dia'), ('noche', 'noche'), ('ambos', 'ambos')], max_length=100, verbose_name='Control de esfinteres')),
                ('actividades_familiares', models.TextField(blank=True, null=True, verbose_name='Actividades Familiares')),
                ('comportameinto_en_casa', models.TextField(blank=True, null=True, verbose_name='Comportamiento en casa')),
                ('castigos', models.CharField(blank=True, max_length=100, null=True, verbose_name='¿Castigan al niño?')),
                ('juegos_habituales', models.TextField(blank=True, null=True, verbose_name='Juegos Habituales')),
                ('seguir_reglas', models.CharField(blank=True, max_length=200, null=True, verbose_name='Adaptación a las reglas')),
                ('tiempo_tv_tablet', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cúanto tiempo ve tv u otro equipo')),
                ('se_viste', models.CharField(blank=True, max_length=100, null=True, verbose_name='Se viste solo')),
                ('tutela', models.TextField(blank=True, null=True, verbose_name='Tutela del menor ')),
                ('parestesco_tutor', models.CharField(blank=True, max_length=100, null=True, verbose_name='Se viste solo')),
                ('registro', models.DateField(auto_now_add=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='static/pupils/')),
                ('folio', models.CharField(default='', max_length=200)),
                ('grado', models.ForeignKey(on_delete=direction.models.Grado, to='direction.Grado')),
                ('grupo', models.ForeignKey(blank=True, null=True, on_delete=direction.models.Grupo, to='direction.Grupo')),
                ('parenttutor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='direction.PadreTutor')),
            ],
        ),
    ]
