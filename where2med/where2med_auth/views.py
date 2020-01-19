from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group

from .forms import LoginForm, SignupForm_Patient, SignupForm_MedicalCenter
from home_page import urls
from .models import Patient, MedicalCenter, Admin

# Create your views here.
def Login(request):
    if request.user.is_authenticated:
        return redirect("index_home_page")

    message = "Not Login"
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                message = "User logged"
                return redirect("index_home_page")
            else:
                message = "Username or password is not correct"
        else:
            message = "Invalid form"
    context = {"form": form, "message": message}

    return render(request, "where2med_auth/login.html",context)

def Logout(request):
    logout(request)
    return redirect("login")


def Signup_Patient(request):
    if request.user.is_authenticated:
        return redirect("index_home_page")

    message = ""
    form = SignupForm_Patient()
    if request.method == "POST":
        form = SignupForm_Patient(request.POST or None)
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password == confirm_password:
            if form.is_valid():
                user = User.objects.create_user(
                    username=request.POST["username"], email=request.POST["email"]
                )
                user.set_password(password)
                # add user to users group
                user_group = Group.objects.get(name="Patient")
                user.groups.add(user_group)
                # user is not staff
                user.is_staff = False
                # user is not superuser
                user.is_superuser = False
                # user is active
                user.is_active = True
                # save
                user.save()

                #create patitient
                patient = Patient.objects.create(
                    user=user
                )

                patient.save()

                # login after signup
                user = authenticate(
                    request, username=request.POST["username"], password=password
                )
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect("index_home_page")
                    else:
                        message = "User is not active"
                else:
                    message = "User not signup correctly"

            else:
                message = "Invalid form"
        else:
            message = "Passwords are not equals"
    context = {"form": form, "message": message}
    return render(request, "where2med_auth/signup.html", context)

def Signup_MedicalCenter(request):
    if request.user.is_authenticated:
        return redirect("index_home_page")

    message = ""
    form = SignupForm_MedicalCenter()
    if request.method == "POST":
        form = SignupForm_MedicalCenter(request.POST or None)
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password == confirm_password:
            if form.is_valid():
                #create patitient
                medical_center = MedicalCenter.objects.create(
                    cost_per_consult = request.POST["cost_per_consult"]
                )
                medical_center.name = request.POST["name"]
                medical_center.address = request.POST["address"]
                medical_center.city = request.POST["city"]
                medical_center.phone = request.POST["phone"]
                #medical_center.image= request.POST["image"]
                #medical_center.cost_per_consult = request.POST["cost_per_consult"]
                medical_center.save()

                user = User.objects.create_user(
                    username=request.POST["username"], email=request.POST["email"]
                )

                user.set_password(password)
                # add user to users group
                user_group = Group.objects.get(name="MedicalCenterAdmin")
                user.groups.add(user_group)
                # user is not staff
                user.is_staff = False
                # user is not superuser
                user.is_superuser = False
                # user is active
                user.is_active = True
                # save
                user.save()

                #create patitient
                admin = Admin.objects.create(
                    user=user,
                    medical_center=medical_center
                )

                admin.save()

                # login after signup
                user = authenticate(
                    request, username=request.POST["username"], password=password
                )
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect("index_home_page")
                    else:
                        message = "User is not active"
                else:
                    message = "User not signup correctly"

            else:
                message = "Invalid form"
        else:
            message = "Passwords are not equals"
    context = {"form": form, "message": message}
    return render(request, "where2med_auth/signup.html", context)