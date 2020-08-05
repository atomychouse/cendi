from django.contrib import admin
from direction.models import (School, Grado, 
    Grupo, PadreTutor, Alumno)
# Register your models here.
admin.site.register(School)
admin.site.register(Grado)
admin.site.register(PadreTutor)

'''
class GrupoAdmin(admin.ModelAdmin):
    change_list_template = 'admin/grupo_list.html'
    list_display = ['name','grade','horario','alumnos']
    def get_queryset(self, request):
        return super(GrupoAdmin,self).get_queryset(request).select_related('alumno')
    def alumnos(self, obj):
        return obj.alumno_set.all().count()
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        return response

class AlumnoAdmin(admin.ModelAdmin):
    #exclude = ('folio',)
    change_list_template = 'admin/alumno_list.html'
    list_display = ['folio', 'curp', 'apaterno', 'amaterno','nombre',]
    fieldsets = (
            ('Datos Generales', {
                'fields': (
                    ('foto'),
                    ('apaterno', 'amaterno'), ('nombre', 'curp'),
                    ('lugar_nacimeinto','genero',),
                    ('nacimiento',),
                    ('grado','grupo',),
                    ('otra_escuela',),
                    ('domicilio',),
                    ('tutela', 'parestesco_tutor'),
                    ('parenttutor',),
                )
            }),
            ('Salud', {
                'classes': ('collapse',),
                'fields': (
                    ('peso_al_nacer','talla_al_nacer',),
                    ('peso', 'medida',),
                    ('tipo_desangre', 'enfermedad_cronica',),
                    ('goples','esfinteres',),
                    ('alergias','alimentacion',),
                    ),
            }),
          ('Otros Datos', {
                'classes': ('collapse',),
                'fields': (
                    ('actividades_familiares','comportameinto_en_casa',),
                    ('castigos', 'seguir_reglas',),
                    ('juegos_habituales', 'tiempo_tv_tablet',),
                    ('se_viste',),
                    ),
            }),
        )

    def changelist_view(self, request, extra_context=None):
        grupos = Grupo.objects.all()
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            response.context_data['grupos'] = grupos
        except:
            pass
        return response

'''


