import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import SignUpForm
from .models import User



def get_users_list(request):
    users_list = User.objects.all()
    output = (' | ').join(i.email for i in users_list)
    return HttpResponse(output)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def loginuser(request):

    return render(request, 'login.html')


def create(request):
    data = json.loads(request.body)
    new_user = User.objects.create(**data)
    return HttpResponse(f'{request.method} method activated! Added new user where id={new_user.id}.')


def delete(request):
    data = json.loads(request.body)
    try:
        user = User.objects.get(id=data['id'])
        user.delete()
        return HttpResponse(f'{request.method} method activated! Deleted user where id={data["id"]}.')
    except User.DoesNotExist:
        return HttpResponse(f'Sorry, but user where id={data["id"]} does not exist')


def retrieve(request):
    data = json.loads(request.body)
    try:
        user = User.objects.get(id=data['id'])
    except User.DoesNotExist:
        return HttpResponse(f'Sorry, but user where id={data["id"]} does not exist')
    else:
        return HttpResponse(f'{request.method} method activated! You chose user #{user.id}:"{user.title}"')


def update_user(request):
    data = json.loads(request.body)
    try:
        user = User.objects.get(id=data['id'])
        for key in data.keys():
            if key in user.__dict__.keys():
                user.__dict__[key] = data[key]
        user.save()
        return HttpResponse(f'{request.method} method activated! The user #{user.id} was updated"')
    except User.DoesNotExist:
        return HttpResponse(f'Sorry, but user where id={data["id"]} does not exist')
