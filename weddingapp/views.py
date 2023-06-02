from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'homepage.html')
def about(request):
    return render(request,'aboutpage.html')
def homepage(request):
    return render(request,'homepage.html')
def gallery(request):
    return render(request,'gallery.html')
def con(request):
    return render(request,'contact.html')