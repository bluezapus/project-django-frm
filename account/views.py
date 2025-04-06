from django.shortcuts import render, redirect
from django.contrib.auth import logout

from . forms import RegisterUserForms, UpdateUserForm

# Create your views here.
def index_profiles(request):
     context = {
          'title': 'data profile',
     }
     return render(request, 'account/profile.html', context)

def update_Profiles(request):
    if request.method == 'POST':
        form =UpdateUserForm(request.POST or None, request.FILES or None, instance=request.user) # update img_usr use FILES
        if form.is_valid():
            form.save()
            return redirect('/accounts/')
    else:
        form =UpdateUserForm(instance=request.user)

    context = {
          'title': 'update data profile',
          'form': form,
    }
    return render(request, 'account/edit_profile.html', context)

def register_users(request):
    if request.method == "POST":
        form = RegisterUserForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') # rediret to home if successfully
        
    else:
            form = RegisterUserForms()

    context = {
        'register': 'Register User',
        'form': form,
    }
    return render(request, 'registration/register.html', context) #take the global templates registration

def LogoutView(request):
    logout(request)
    return redirect('/')