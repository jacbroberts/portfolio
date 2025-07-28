from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import os

def is_spam(message):
    spam = False
    malware = False
    spam_words = ["price", "SEO", "free", "deadline","urgent"]
    possible_malware_words = ["script.google.com","https","http"]
    if any(word in message.lower() for word in spam_words):
        spam = True
    if any(word in message.lower() for word in possible_malware_words):
        malware = True
    if malware:
        return "Possible Malware "
    if spam:
        return "SPAM "+ message
    return message
    

# Create your views here.
def index(request):
    if request.method == "POST":
        s_email = os.environ['EMAIL_USERNAME']
        email = request.POST.get("email")
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        subject = f"[{email}]: " + request.POST.get("subject")
        subject = is_spam(subject)
        message = f"{first_name} {last_name} \n\n" + request.POST.get("message")
        message = is_spam(message)
        print(message)
        send_mail(
            subject,
            message,
            s_email,
            [s_email],
            fail_silently=False,
        )

    return render(request, "home.html")