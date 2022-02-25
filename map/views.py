from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail


def Email(request):
	if request.method == 'POST':
		message = request.POST['message']
		send_mail('Contact Form',
		 message, 
		 settings.EMAIL_HOST_USER,
		 ['donthireddytejareddy17@gmail.com'], 
		 fail_silently=False)
	return render(request, 'email.html')

# Create your views here.
def Map(request):
    return render(request,'map.html')

