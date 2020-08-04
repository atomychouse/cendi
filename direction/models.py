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
    nivel = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre


class Grupo(models.Model):
    name = models.CharField(u'GRUPO', max_length=10)
    grade = models.ForeignKey(Grado, on_delete=models.CASCADE)
    horario = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class PadreTutor(models.Model):
    autorizado = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='static/padres_tutores', blank=True, null=True)
    nombre_completo = models.TextField(u'Nombre Completo')
    edad = models.IntegerField(u'Edad', default='')
    folio = models.CharField(u'Folio',max_length=40)
    
class Alumno(models.Model):
    apaterno = models.CharField(u'A. Paterno', max_length=200)
    amaterno = models.CharField(u'A. Materno',max_length=200,default="")
    nombre = models.CharField(u'Nombre', max_length=200,default='')
    curp = models.CharField(u'CURP', max_length=200, unique=True)
    nacimiento = models.DateField(u'Fecha Nacimiento')
    genero = models.CharField(u'Genero',max_length=10,choices=(('masculino','Masculino'),('femenino','Femenino')))
    lugar_nacimeinto = models.CharField(u'Lugar nacimeinto', max_length=500)
    domicilio = models.TextField(u'Domicilio')
    peso = models.CharField(u'Peso', max_length=10)
    medida = models.CharField(u'Medida', max_length=10)
    tipo_desangre = models.CharField(u'Tipo Sangre', max_length=10)
    grado = models.ForeignKey(u'Grado',Grado)
    grupo = models.ForeignKey(u'Grupo',Grupo, blank=True, null=True)
    otra_escuela = models.CharField(blank=True, max_length=500, null=True)
    peso_al_nacer = models.CharField(u'Peso al nacer', max_length=10, blank=True, null=True)
    talla_al_nacer = models.CharField(u'Medida al nacer', max_length=10, blank=True, null=True)
    enfermedad_cronica = models.CharField(u'Enfermedad Crónica', max_length=500, blank=True, null=True)
    alergias = models.CharField(u'Alergias', max_length=500, blank=True, null=True)
    goples = models.CharField(u'Golpes en la cabeza', max_length=200, blank=True, null=True)
    alimentacion = models.CharField(u'Alimentación', max_length=200, blank=True, null=True)
    esfinteres = models.CharField(u'Control de esfinteres', max_length=100, choices=(('dia','dia'),('noche','noche'), ('ambos','ambos'),) )
    actividades_familiares = models.CharField(u'Actividades Familiares', max_length=500, blank=True, null=True)
    comportameinto_en_casa = models.CharField(u'Comportamiento en casa', max_length=500, blank=True, null=True)
    castigos = models.CharField(u'¿Castigan al niño?', max_length=100, blank=True, null=True)
    juegos_habituales = models.CharField(u'Juegos Habituales', max_length=500, blank=True, null=True)
    seguir_reglas = models.CharField(u'Adaptación a las reglas', max_length=200, blank=True, null=True)
    tiempo_tv_tablet = models.CharField(u'Cúanto tiempo ve tv u otro equipo', max_length=100, blank=True, null=True)
    se_viste = models.CharField(u'Se viste solo', max_length=100, blank=True, null=True)
    tutela = models.CharField(u'Tutela del menor ', max_length=500, blank=True, null=True)
    parestesco_tutor = models.CharField(u'Se viste solo', max_length=100, blank=True, null=True)
    registro = models.DateField(auto_now_add=True)
    foto = models.ImageField(upload_to='static/pupils/', blank=True, null=True)
    folio = models.CharField(max_length=200,default='', blank=True, null=True)
    parenttutor = models.ForeignKey(PadreTutor, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '%s %s %s %s '%(self.apaterno, self.amaterno, self.nombre, self.folio)

    def gen_folio(self):
        d = datetime.now()
        folio = '%s%s%s%s%s%s'%(str(d.year)[:2], 
                                d.month, 
                                d.day, 
                                d.hour, 
                                d.minute, 
                                d.second)
        folio = int(folio)
        folio = hex(folio).upper()
        return folio

    def save(self, *args, **kwargs):
        self.folio = self.gen_folio()        
        super(Alumno, self).save(*args, **kwargs)
