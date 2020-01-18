from django.shortcuts import render

# Create your views here.
def Login(request):
    return render(request, "where2med_auth/file.html", {})

def Logout(request):

    return render(request, "where2med_auth/file.html", {})

def Signup(request):

    return render(request, "where2med_auth/file.html", {})