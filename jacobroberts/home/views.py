from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import os
from home.models import Page, Entry, TimeEntry, Post, Skill

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
    pages = Page.objects.all()

    # if request.method == "POST":
    #     s_email = os.environ['EMAIL_USERNAME']
    #     email = request.POST.get("email")
    #     first_name = request.POST.get("fname")
    #     last_name = request.POST.get("lname")
    #     subject = f"[{email}]: " + request.POST.get("subject")
    #     subject = is_spam(subject)
    #     message = f"{first_name} {last_name} \n\n" + request.POST.get("message")
    #     message = is_spam(message)
    #     print(message)
    #     send_mail(
    #         subject,
    #         message,
    #         s_email,
    #         [s_email],
    #         fail_silently=False,
    #     )

    return render(request, "home.html",{"pages":pages})

def education(request):
    return render(request, "education.html")

def experience(request):
    return render(request, "experience.html")

def page(request, name):
    name = name.lower()
    #verify that name is a page
    pages = Page.objects.all()
    p = Page.objects.filter(name__iexact=name)  
    if p.exists():
        data = []
        p = p[0]
        if p.type == Page.TIMELINE:
            entries = Entry.objects.filter(page=p)
            
            for entry in entries:
                info = TimeEntry.objects.get(entry=entry)
                data.append({"title":entry.title,
                     "subtitle":info.subtitle,
                     "start_data":info.start_date,
                     "end_date":info.end_date,
                     "body":info.body})
                
            return render(request, "timeline.html",{"data":data,"pages":pages})
                
        elif p.type == Page.BLOG:
            return render(request,"blog.html",{"pages":pages})
        elif p.type == Page.SKILL:
            return render(request, "skills.html",{"pages":pages})
        else:
            return render(request, "404.html",{"pages":pages})

    else:
        return render(request, "404.html",{"pages":pages})

    

    
