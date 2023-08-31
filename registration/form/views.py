from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from . models import EventRegistration
from django.contrib import messages
def register(request):
    if request.method == 'POST' and request.FILES:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        dob = request.POST['dob']
        signature = request.POST['signature']
        inspiration = request.POST['inspiration']
        art_works = request.FILES['art_works']
        if EventRegistration.objects.filter(phone=phone):
            messages.error(request, "You have already applied for this program, pls check your mail or spam.")
        elif EventRegistration.objects.filter(email=email):
            messages.error(request, "You have already applied for this program, pls check your mail or spam.")  
        else:        
            event = EventRegistration.objects.create(
                name=name,
                email=email,
                phone=phone,
                address=address,
                dob=dob,
                signature=signature,
                inspiration=inspiration,
                art_works=art_works,
            )
            event.save()
            subject = 'Application Sent Successfully'
            message = f'Hi {name}, we have recieved your application, \nWe will review and get back to you\nThank You!!!'
            email_from = 'Artention <vybrantalpha@gmail.com>'
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            #To admins
            header = f'Artention application from {name}'
            content = f'{name}, has submitted the application for the Upcycling Artention'
            system_mail = 'Artention <vybrantalpha@gmail.com>'
            admin_mail = ['felixbotwe194@gmail.com']
            send_mail( header, content, system_mail, admin_mail )
            # messages.success(request, f'Dear {name}, your application has been sent successfully.')
            return redirect('success')
    

    return render(request, 'index.html')


def success(request):
    return render(request, 'success.html')
