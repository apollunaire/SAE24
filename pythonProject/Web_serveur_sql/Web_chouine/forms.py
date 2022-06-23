from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class CapteurForms(ModelForm):
    class Meta:
        model = models.Capteur
        fields = {'emplacement', 'date'}
        labels = {
            'emplacement': _('Emplacement'),
            'date': _('Date'),
        }

