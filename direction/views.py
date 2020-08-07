# -*- encoding: utf-8 -*-

from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from direction.models import (Alumno, PadreTutor)
from school.utils import (FormCreator, Commonds)
from django import forms

FIELDS_ALUMNO = ['nombre', 'apaterno', 'amaterno', 'genero', 'curp', 'nacimiento', 'tipo_desangre', 'alergias']
FIELDS_TUTOR = ['nombre_completo','edad','folio']
FORM  = FormCreator()

#class Home(LoginRequiredMixin, TemplateView):
class Home(TemplateView):
    #login_url = '/direccion/login/'
    def get(self, request):
        context = {}
        return render(request, 'direction/index.html', context)

class Login(TemplateView):
    template_name = "login.html"

    def get(self, request):
        context = {}
        
        return render(request, 'direction/login.html', context)

class Inscripcion(TemplateView):
    #login_url = '/direccion/login/'
    modelos = [Alumno,PadreTutor]
    fields = {'alumno':FIELDS_ALUMNO, 'tutor':FIELDS_TUTOR}
    general_form  = FormCreator()
    widgets_alumno = {
        'nacimiento': forms.TextInput(attrs={'type':'date',
                                         'class':'form-control'}),
    }

    def format_form(self, fields, forma):
        for l in fields:
            label = forma.base_fields.get(l).label
            forma.base_fields.get(l).widget.attrs={'class':'form-control',
                'placeholder':label
            }

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

    def post(self, request):
        data = request.POST.copy()
        paso=int(data['step'])
        pk = data.get('id',None)
        instanced = None
        folio = 0
        if len(pk)>0:
            instanced = Alumno.objects.get(id=pk)
        pasos = [self.fields['alumno'],self.fields['tutor']]
        modelo = self.modelos[paso]
        campos = pasos[paso]
        form = self.general_form.form_to_model(modelo=modelo,fields=campos)
        form = form(data, instance=instanced)
        if form.is_valid():
            f = form.save()
            if paso==0 and not instanced:
                f.folio = self.gen_folio()
                f.save()

            response = {'id':f.id, 'folio':f.folio}
            return JsonResponse(response)
        else:
            response = {'errors':form.errors.get_json_data()}
            return JsonResponse(response)


    def get(self, request):
        context = {}
        form_alumno = self.general_form.form_to_model(modelo=Alumno, 
                                              excludes=[], 
                                              widgets=self.widgets_alumno)
        self.format_form(self.fields['alumno'], form_alumno)                                                     
        form_tutor = self.general_form.form_to_model(modelo=PadreTutor, 
                                              fields=self.fields['tutor'])

        self.format_form(self.fields['tutor'], form_tutor)                                                     
        context['form_alumno'] = form_alumno
        context['form_tutor'] = form_tutor
        return render(request, 'direction/inscripcion.html', context)

class AddTutor(TemplateView, Commonds):
    def post(self, request):
        context = {}
        data = request.POST.copy()
        instanced = None
        try:
            idp = request.POST.get('id_parent')
            instanced = PadreTutor.objects.get(pk=idp)
            data['folio'] = instanced.folio
        except:
            data['folio'] = self.gen_folio()
        form = FORM.form_to_model(modelo=PadreTutor, excludes=[])
        form = form(data, instance=instanced)
        if form.is_valid():
            if not instanced:
                user = User.objects.create_user(username=data['folio'],
                                 email='%s@cendipiaget.com'%(data['folio']),
                                 is_staff=True,
                                 password=data['folio'])
            f = form.save()
            callbacks = ['activate_paso_dos',]
            response = {'id':f.id, 'folio':f.folio, 'callbacks':callbacks}
            return JsonResponse(response)
        else:
            response = {'errors':form.errors.get_json_data()}
            return JsonResponse(response)

class AddAlumno(TemplateView, Commonds):
    def post(self, request):
        context = {}
        data = request.POST.copy()
        data['folio'] = self.gen_folio()
        instanced = None
        form = FORM.form_to_model(modelo=Alumno, excludes=[])
        form = form(data, instance=instanced)
        if form.is_valid():
            f = form.save()
            try:
                f.foto = request.FILES.get('foto')
                f.save()
            except:
                pass
            callbacks = ['activate_paso_tres',]
            response = {'id':f.id, 'folio':f.folio, 'callbacks':callbacks}
            return JsonResponse(response)
        else:
            response = {'errors':form.errors.get_json_data()}
            return JsonResponse(response)
