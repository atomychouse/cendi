# -*- encoding: utf-8 -*-

from direction.models import (Alumno, PadreTutor)
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import (render, redirect, get_object_or_404)
from django.views.generic.base import TemplateView
from school.utils import (FormCreator)


FIELDS_ALUMNO = ['nombre', 'apaterno', 'amaterno', 'genero', 'curp', 'nacimiento', 'tipo_desangre', 'alergias']
PASO_1 = []
FIELDS_TUTOR = ['nombre_completo','edad','folio']

class Home(TemplateView):
    def post(self, request):
        context = {}
        data = request.POST.copy()
        folio = data.get('folio', None)
        if folio: 
            try: 
                user = User.objects.get(username=folio)
            except:
                context['err'] = 'El folio no corresponde a un usuario valido. :('
                return render(request, 'webapp/index.html', context)
            
            user = authenticate(username=user.username, password=folio)
            if user: 
                login(request, user)
                return redirect('parent')
            else:
                context['err'] = 'El folio no corresponde a un usuario valido. :('
                return render(request, 'webapp/index.html', context)
                
            context['uss'] = user
        else:
            context['err'] = 'El folio no corresponde a un usuario valido. :('
        return render(request, 'webapp/index.html', context)

    def get(self, request):
        context = {}
        if request.user.is_staff:
            return redirect('parent')
        return render(request, 'webapp/index.html', context)

class Inscribete(TemplateView,):
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
                                              excludes=['folio', 'parenttutor','eliminado'],
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


class AuthParent(TemplateView):

    def post(self, request):
        data = request.POST.copy()
        folio = data.get('folio', None)
        if folio: 
            user = User.objects.get(username=folio)


class ParentHome(LoginRequiredMixin, TemplateView):
    general_form  = FormCreator()
    login_url = '/'
    def get(self, request):
        context = {}
        widgets_paso2 = {
        'nacimiento': forms.TextInput(attrs={
            'type':'date',
            'class':'form-control form-control-user'
            }),
        }

        parent = get_object_or_404(PadreTutor, folio=request.user.username) 
        form_paso_dos = self.general_form.form_to_model(modelo=Alumno, 
                                              excludes=['folio', 'parenttutor', 'eliminado'],
                                              widgets=widgets_paso2
                                              )
        for f in form_paso_dos.base_fields:
            form_paso_dos.base_fields.get(f).widget.attrs={'class':'form-control form-control-user',
            }
        form_paso_dos.base_fields.get('curp').widget.attrs={
            'class':'form-control form-control-user curp',
            'id':'alumno_curp',
            'maxlength':'18'
            }
        context['paso2'] = form_paso_dos
        context['parent'] =  parent
        context['alumnos'] = parent.alumno_set.filter(eliminado=False)
        return render(request, 'webapp/parent.html', context)

class ParentPagos(LoginRequiredMixin, TemplateView):
    login_url = '/'
    def get(self, request):
        pagos = [
            {
                'pk':100,
                'name':u'Inscripción',
                'monto':'1200',
                'status':0,
                'start':'',
                'limite_pago':'24/10/2020'
            }
        ]

        for x in range(1,10):
            pago = {
                'pk':x,
                'name':u'Colegiatura %s'%(x),
                'monto':'800',
                'status':x,
                'start':'',
                'limite_pago':'24/%s/2020'%(x)
            }
            pagos.append(pago)

        context = {}
        parent = get_object_or_404(PadreTutor, folio=request.user.username) 
        context['parent'] =  parent
        context['pagos'] = pagos
        return render(request, 'webapp/parent_pagos.html', context)


class rmAlumno(TemplateView):
    def get(self, request, folio):
        context = {}
        try:
            a = Alumno.objects.get(folio=folio)
            a.eliminado = True
            a.save()
        except:
            pass
        return redirect('/')


class Logout(TemplateView):
    def get(self, request):
        logout(request)
        context = {}
        return redirect('/')


