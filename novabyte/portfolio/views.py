from django.shortcuts import render
from .models import Project
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# Create your views here.

def home(request):
    return render(request, 'portfolio/index.html')

def about(request):
    return render(request, 'portfolio/about.html')

def contact(request):
    return render(request, 'portfolio/contact.html')
    
def projects(request):
    projects = Project.objects.all()  # Assuming Project is the model for projects
    print(projects)
    return render(request, 'portfolio/projects.html', {'projects': projects})

def project(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'portfolio/project.html', {'project': project})


def contact_submit(request):
    try:
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['first-name']
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']
                company = form.cleaned_data['company']
                phone_number = form.cleaned_data['phone-number']
                send_mail(
                    f'New message from {name}',
                    f'Name: {name}\nEmail: {email}\nCompany: {company}\nPhone Number: {phone_number}\n\nMessage:\n{message}',
                    settings.COMPANY_EMAIL,
                    [settings.COMPANY_EMAIL],
                    fail_silently=False,
                )
                return render(request, 'portfolio/index.html')
    except Exception as e:
        print(f"Failed to send email: {e}")
    form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})
