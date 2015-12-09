from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth

from models import Advocate, Single_Profile
from forms import RegistrationForm, AuthenticationForm

def home(request):
    return render_to_response('profiles/0home.html')

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
        template_name = 'profiles/registration.html'
    return render(request, template_name, {'form': form})

def login(request):
    if request.method != 'POST':
        form = AuthenticationForm()
        template_name = 'profiles/login.html'
        return render(request, template_name, {'form': form})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None :
            auth.login(request, user)
            return HttpResponseRedirect('/advocate')
        else:
            return HttpResponse("Your username and password didn't match.")

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def advocate_homepage(request):
    users_singles = Single_Profile.objects.filter(created_by = request.user)

    template_name = 'profiles/advocate_homepage.html'
    context = {'user': request.user, 'singles':users_singles}
    return render(request, template_name, context)

class AdvocateCreate(CreateView):
    model = Advocate
    fields = ['user', 'email']
    success_url = reverse_lazy('home')

class AdvocateUpdate(UpdateView):
    model = Advocate
    fields = ['user', 'email']
    success_url = reverse_lazy('home')

class SingleCreate(CreateView):
    model = Single_Profile
    fields = ['firstname', 'lastname','gender', 'age', 'photo' ]
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # form.instance.created_by = self.request.user
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.most_recent_change_id = 0
        self.object.save()
        return redirect('home')


class SingleUpdate(UpdateView):
    template_name = 'profiles/single_profile_form.html'
    model = Single_Profile
    fields = ['firstname', 'lastname','gender', 'age', 'photo']
    success_url = reverse_lazy('home')


