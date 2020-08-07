from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class School(models.Model):
    school_name = models.CharField(max_length=300)
    location = models.TextField()
    logo = models.ImageField(upload_to='static/images', blank=True, null=True)
    def __str__(self):
        return self.school_name


class Grado(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre


class Grupo(models.Model):
    name = models.CharField(u'GRUPO', max_length=10)
    def __str__(self):
        return self.name

class PadreTutor(models.Model):
    parent_apaterno = models.CharField(u'Apellido Paterno', max_length=200)
    parent_amaterno = models.CharField(u'Apellido Materno',max_length=200,default="")
    parent_nombre = models.CharField(u'Nombre(s)', max_length=200,default='')
    parent_curp = models.CharField(u'CURP', max_length=200, unique=True)
    parent_nacimiento = models.DateField(u'Fecha Nacimiento')
    parentesco = models.CharField(u'Parentesco',max_length=100)
    parent_domicilio = models.TextField(u'Domicilio')
    folio = models.CharField(u'Folio',max_length=40, blank=True, null=True)
    tutela = models.BooleanField(default=True)
    dateadd = models.DateField(auto_now_add=True)

class Alumno(models.Model):
    eliminado = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='static/pupils/', blank=True, null=True)
    apaterno = models.CharField(u'Apellido Paterno', max_length=200)
    amaterno = models.CharField(u'Apellido Materno',max_length=200,default="")
    nombre = models.CharField(u'Nombre(s)', max_length=200,default='')
    curp = models.CharField(u'CURP', max_length=200, unique=True)
    genero = models.CharField(u'Sexo',max_length=10,choices=(('masculino','Masculino'),('femenino','Femenino')))
    nacimiento = models.DateField(u'Fecha Nacimiento')
    lugar_nacimeinto = models.CharField(u'Lugar nacimeinto', max_length=500)
    domicilio = models.TextField(u'Domicilio')
    peso = models.CharField(u'Peso', max_length=10)
    medida = models.CharField(u'Medida', max_length=10)
    tipo_desangre = models.CharField(u'Tipo de Sangre', max_length=10)
    grado = models.ForeignKey(Grado, u'Grado al que se inscribe')
    otra_escuela = models.CharField(u'Ha asistido a otra escuela', blank=True, max_length=500, null=True)
    peso_al_nacer = models.CharField(u'¿Cuánto peso al nacer?', max_length=10, blank=True, null=True)
    talla_al_nacer = models.CharField(u'¿Cuánto midio al nacer?', max_length=10, blank=True, null=True)
    enfermedad_cronica = models.CharField(u'¿Tiene alguna enfermedad Crónica? ¿Cuál?', max_length=500, blank=True, null=True)
    alergias = models.CharField(u'¿Es alérgico a algo?', max_length=500, blank=True, null=True)
    goples = models.CharField(u'¿Sufrió algun golpe en la cabeza?', max_length=200, blank=True, null=True)
    alimentacion = models.CharField(u'¿Come todo tipo de alimentos?', max_length=200, blank=True, null=True)
    esfinteres = models.CharField(u'Controla  esfinteres', max_length=100, choices=(('no','aun no'), ('dia','de dia'),('noche','de noche'), ('ambos','ambos'),) )
    actividades_familiares = models.CharField(u'¿Qué actividades realiza en familia?', max_length=500, blank=True, null=True)
    comportameinto_en_casa = models.CharField(u'¿Cómo describiria el comportamiento del niño(a) en casa?', max_length=500, blank=True, null=True)
    castigos = models.CharField(u'¿Castigan al niño?', max_length=100, blank=True, null=True)
    juegos_habituales = models.CharField(u'¿A qué juega habitualmente?', max_length=500, blank=True, null=True)
    seguir_reglas = models.CharField(u'¿Qué tanto se adapta a las reglas del juego?', max_length=200, blank=True, null=True)
    tiempo_tv_tablet = models.CharField(u'¿Cuánto tiempo ve televisión, internet o algun otro tipo de entretenimiento?', max_length=100, blank=True, null=True)
    se_viste = models.CharField(u'¿Se viste solo o quien lo ayuda?', max_length=100, blank=True, null=True)
    tutela = models.CharField(u'Tutela del menor ', max_length=500, blank=True, null=True)
    registro = models.DateField(auto_now_add=True)
    folio = models.CharField(max_length=200,default='', blank=True, null=True)
    parenttutor = models.ForeignKey(PadreTutor, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '%s %s %s %s '%(self.apaterno, self.amaterno, self.nombre, self.folio)
