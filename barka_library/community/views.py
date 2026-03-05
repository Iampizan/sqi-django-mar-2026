from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def events(request):
    content = """
    <section>
        <h2>Upcoming Community Events</h2>
        <p>Book Reading - Saturday 10AM</p>
        <p>Children's Story Hour - Sunday 2PM</p>
    </section>
    """
    return HttpResponse(content)
