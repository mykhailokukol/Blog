from django import forms
from . import models
from IndexApp import models as index_models


class MessageForm(forms.ModelForm):

    class Meta:

        model = models.Message
        fields = ['text', 'image']
        widgets = {
            #
        }
