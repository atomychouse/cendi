# -*- encoding: utf-8 -*-

from direction.models import (Alumno, PadreTutor)
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import TemplateView
from school.utils import (FormCreator)

FIELDS_ALUMNO = ['nombre', 'apaterno', 'amaterno', 'genero', 'curp', 'nacimiento', 'tipo_desangre', 'alergias']
PASO_1 = []
FIELDS_TUTOR = ['nombre_completo','edad','folio']

class Home(TemplateView):
    template_name = "home.html"

    def get(self, request):
        context = {}
        return render(request, 'webapp/index.html', context)

class Auth(TemplateView,):
    general_form  = FormCreator()

    def get(self, request):
        folio = request.GET.get('f', None)
        instanced = None
        if folio: 
            instanced = PadreTutor.objects.get(folio=folio)
        
        context = {}
        widgets_paso1 = {
        'parent_nacimiento': forms.TextInput(attrs={'type':'date',
                                         'class':'form-control form-control-user'}),
        'curp': forms.TextInput(attrs={
            'id':'parent_curp',
            'class':'curp form-control form-control-user'
        })
        }
        widgets_paso2 = {
        'nacimiento': forms.TextInput(attrs={
            'type':'date',
            'class':'form-control form-control-user'
            }),
        }
        form_paso_uno = self.general_form.form_to_model(modelo=PadreTutor, 
                                              excludes=['folio'],
                                              widgets=widgets_paso1 
                                              )
        form_paso_dos = self.general_form.form_to_model(modelo=Alumno, 
                                              excludes=['folio', 'parenttutor'],
                                              widgets=widgets_paso2
                                              )
        for f in form_paso_uno.base_fields:
            form_paso_uno.base_fields.get(f).widget.attrs={'class':'form-control form-control-user',
            }
        for f in form_paso_dos.base_fields:
            form_paso_dos.base_fields.get(f).widget.attrs={'class':'form-control form-control-user',
            }
        form_paso_uno.base_fields.get('parent_curp').widget.attrs={
            'class':'form-control form-control-user curp',
            'id':'parent_curp',
            'maxlength':'18'
            }
        form_paso_dos.base_fields.get('curp').widget.attrs={
            'class':'form-control form-control-user curp',
            'id':'alumno_curp',
            'maxlength':'18'
            }
        context['paso1'] = form_paso_uno(instance=instanced)
        context['parent'] = instanced
        context['paso2'] = form_paso_dos

        return render(request, 'webapp/home.html', context)


