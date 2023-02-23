from django.shortcuts import render
from .forms import OpinionForm


def about(request):
    return render(request, 'about.html')


def contact(request):
    opinion_submit_button = request.POST.get("op-sub-btn")
    name = ''
    email = ''
    message = ''

    form = OpinionForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')

    context = {'form': form, 'name': name, 'email': email, 'message': message,
               'opinion_submit_button': opinion_submit_button}
    return render(request, 'contact.html', context)


def index(request):
    return render(request, 'index.html')


def products(request):
    return render(request, 'products.html')


def single(request):
    return render(request, 'single.html')