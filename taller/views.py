from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Taller
# Create your views here.

class TallerPageView(TemplateView):
    template_name = 'taller/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Si se pasa un id a través de la URL, seleccionamos ese taller
        taller_id = self.kwargs.get('id', None)
        
        # Si no se pasa un id, seleccionamos el primer taller disponible
        if taller_id:
            context['taller'] = Taller.objects.filter(id=taller_id).first()
        else:
            context['taller'] = Taller.objects.first()
        
        return context