from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'simple_web/home_page.html')
def profile_page(request):
    return render(request, 'simple_web/profile_page.html')
def service_page(request):
    return render(request, 'simple_web/service_page.html')
def help_page(request):
    return render(request, 'simple_web/help_page.html')
