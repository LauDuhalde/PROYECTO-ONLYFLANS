from django.shortcuts import render,redirect, get_object_or_404
from .models import Flan
from .forms import ContactFormForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html',{'flanes':flanes_publicos})

def about(request):
    return render(request, 'about.html',{})

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html',{'flanes':flanes_privados})

def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactFormForm()
    return render(request, 'contact.html', {'form':form})

def success(request):
    return render(request, 'success.html',{})

def logout_page(request):
    return render(request, 'registration/logout.html',{})

def flanDetail(request, flan_id):
    otros_flanes = Flan.objects.exclude(id=flan_id)
    flan = get_object_or_404(Flan, id=flan_id)
    return render(request, 'flan_detail.html',{'flan':flan, 'otros_flanes':otros_flanes})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup_success')  # Redirige a una página de éxito de registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def signup_success(request):
    return render(request, 'registration/signup_success.html',{})
