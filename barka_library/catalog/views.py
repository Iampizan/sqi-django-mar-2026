from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def book_list(request):
    books= ["Things Fall Apart", "The Joys of Motherhood", "The Famished Road", "Half of a Yellow Sun", "Say You're One of Them"]
    content = "<ul>" + "".join([f"<li>{book}</li>" for book in books]) + "</ul>"
    return HttpResponse(content)

def special_books(request):
    featured_books = ["The Secret Lives of Baba Segi's Wives", "A Grain of Wheat"]
    content = "<div><h3>Featured Books</h3><ul>" + "".join([f"<li>{book}</li>" for book in featured_books]) + "</ul></div>"
    return HttpResponse(content)