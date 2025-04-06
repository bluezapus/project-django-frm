from django.shortcuts import render
from django.core.mail import send_mail
from .forms import SendingEmailForm

from django.conf import settings

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SendingEmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            send_mail(subject, # ini subject
                      f"message from {name} with email <{email}>"
                      f"it's message {message}", 
                      None, #ini dari email
                      [settings.EMAIL_HOST_USER],)
    else:
        form = SendingEmailForm()

    context = {
        'title':'contact',
        'form': form,
    }
    return render(request, 'contact/index.html', context)