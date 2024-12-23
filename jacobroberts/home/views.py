from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import os
# Create your views here.
def index(request):
    if request.method == "POST":
        s_email = os.environ['EMAIL_USERNAME']
        email = request.POST.get("email")
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        subject = f"[{email}]: " + request.POST.get("subject")
        message = f"{first_name} {last_name} \n\n" + request.POST.get("message")
        print(message)
        send_mail(
            subject,
            message,
            s_email,
            [s_email],
            fail_silently=False,
        )

    return render(request, "home.html")