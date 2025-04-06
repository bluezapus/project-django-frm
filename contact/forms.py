from django.forms import ModelForm
from . models import Contact


class SendingEmailForm(ModelForm):
    class Meta:
        model = Contact
        fields = (
            'name', 'email', 'subject', 'message',
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({''
        'class':'form-control border-0 bg-light px-4', 
        'placeholder': 'Input Your Full Name',
        'style': 'height: 55px',
        })

        self.fields['email'].widget.attrs.update({''
        'class':'form-control border-0 bg-light px-4', 
        'placeholder': 'Input Your Full Email',
        'style': 'height: 55px',
        })

        self.fields['subject'].widget.attrs.update({''
        'class':'form-control border-0 bg-light px-4', 
        'placeholder': 'Subject',
        'style': 'height: 55px',
        })

        self.fields['message'].widget.attrs.update({''
        'class':'form-control border-0 bg-light px-4 mb-4', 
        'placeholder': 'Message',
        
        })