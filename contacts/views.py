from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect







# Create your views here.
def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        message = 'from {} \n {}' .format(from_email,message)
        try:
            send_mail(subject, message, from_email, ['danielnjama2015@gmail.com'],fail_silently=False)
            mess= 'Thank you for contacting me. I will get back to you soon.'
            return render(request,'success.html',{'mess':mess})
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        
        #return render(request,'success.html')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')