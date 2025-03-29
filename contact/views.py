from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'contact',
    }
    return render(request, 'contact/index.html', context)