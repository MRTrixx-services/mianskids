from django.shortcuts import render, redirect
from .models import AdmissionEnquiry

def save_enquiry(request):
    AdmissionEnquiry.objects.create(
        parent_name=request.POST.get('parent_name', ''),
        phone=request.POST.get('phone', ''),
        email=request.POST.get('email', ''),
        child_name=request.POST.get('child_name', ''),
        child_age=request.POST.get('child_age', ''),
        program=request.POST.get('program', ''),
        message=request.POST.get('message', ''),
    )

def home(request):
    success = False
    if request.method == 'POST':
        save_enquiry(request)
        success = True
    return render(request, 'home.html', {'success': success})

def about(request):
    return render(request, 'about.html')

def contact(request):
    success = False
    if request.method == 'POST':
        save_enquiry(request)
        success = True
    return render(request, 'contact.html', {'success': success})

