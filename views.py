from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .forms import RegisterForm, VoteForm
from .models import Vote

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()
            send_mail('Welcome to eVoting!', f'Thank you for registering, {user.username}.', None, [user.email])
            login(request, user)
            return redirect('vote')
    else:
        form = RegisterForm()
    return render(request, 'polls/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('vote')
    return render(request, 'polls/login.html')

@login_required
def vote(request):
    voter = request.user
    if hasattr(voter, 'vote'):
        return redirect('results')
    if request.method == 'POST':
        form = VoteForm(voter, request.POST)
        if form.is_valid():
            Vote.objects.create(voter=voter, candidate=form.cleaned_data['candidate'])
            send_mail('Vote Confirmation', 'Thank you for voting!', None, [voter.email])
            return redirect('results')
    else:
        form = VoteForm(voter)
    return render(request, 'polls/vote.html', {'form': form})

@login_required
def results(request):
    votes = Vote.objects.filter(candidate__county=request.user.county,
                                candidate__constituency=request.user.constituency)
    return render(request, 'polls/results.html', {'votes': votes})