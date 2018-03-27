from django.shortcuts import render


def signup(request):
    return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    #need to add route to homepabe and don't forget to logout
    return render(request, 'accounts/signup.html')
