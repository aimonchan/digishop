from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'store/home.html')

def signup(request):
    return render(request, 'store/signup.html')

def signin(request):
    return render(request, 'store/signin.html')
