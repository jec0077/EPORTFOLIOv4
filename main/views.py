from django.shortcuts import render, redirect
from .models import ProjectCard, ExperienceCard
from .forms import ContactForm


def home(request):
    return render(request, 'main/home.html')


def projects(request):
    projs = ProjectCard.objects.all()
    context = {"projs": projs}
    return render(request, 'main/projects.html', context)


def live_resume(request):
    return render(request, 'main/live-resume.html')


def career(request):
    exps = ExperienceCard.objects.all()
    context = {"exps": exps}
    return render(request, 'main/career.html', context)


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form": form}
    return render(request, 'main/contact.html', context)
