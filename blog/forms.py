from django.forms import ModelForm
from . models import Comment

class CommentsForm(ModelForm):
    class Meta:
        model = Comment
        fields = (
            'comments',
            'reply',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['comments'].widget.attrs.update({
            'class':'form-control bg-white border-0',
            'rows':'5',
            'placeholder':'Comment'
        })

        self.fields['reply'].widget.attrs.update({
            'class':'form-control bg-white border-0',
            
            'placeholder':'Reply Comment',
            'style': 'height: 55px',
        })