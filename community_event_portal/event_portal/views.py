from django.shortcuts import render


def home(request):
    return render(request, 'event_portal/home.html')
    
def about(request):
    return render(request, 'event_portal/about.html')

def events(request):
    return render(request, 'event_portal/events.html')

def contact(request):
    return render(request, 'event_portal/contact.html')

