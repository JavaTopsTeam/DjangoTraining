from django.forms import ModelForm, Textarea
from .models import *

class UserRegister(ModelForm):
    class Meta:
        model = newuser
        fields = '__all__'
        labels = {
            'first_name': 'First Name'
        }
        error_messages = {
            'first_name': {
                'max_length': "This writer's name is too long."
            },
        }
