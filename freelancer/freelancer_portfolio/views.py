from django.shortcuts import render

# Create your views here.
def services(request):
    return render(request, 'freelancer_portfolio/services.html')
def testimonials(request):
    context = {
        "John Smith": "Excellent work! My website was delivered on time.",
        "Sarah Johnson": "Very professional freelancer with strong Django skills.",
        "Michael Brown": "Helped scale our backend infrastructure efficiently."
    }
    return render(request, 'freelancer_portfolio/testimonials.html', context)
def case_studies(request):

    return render(request, 'freelancer_portfolio/case_studies.html')
def blog(request):

    return render(request, 'freelancer_portfolio/blog.html')
def pricing(request):
    context = {
        "pricing_data": {
            "Basic Website": "$500",
            "Full Stack Web App": "$1500",
            "API Development": "$800",
            "Maintenance Package": "$200/month"
        }
    }
   
    return render(request, 'freelancer_portfolio/pricing.html', context)