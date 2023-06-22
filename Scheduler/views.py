from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login , logout
from .forms import LoginForm, Add_Course_Form,Assign_Lecture_Form, Add_Instructor_Form, Instructor_Login_Form
from . models import Instructor,Lectures
from django.contrib import messages

# Create your views here.

def Home_View(request):
    return render(request,"Scheduler/Home.html")

def Admin_Home_View(request):
    return render(request, "Scheduler/Admin_Home.html")

def Instructors_View(request):
    data = Instructor.objects.all()
    context = {"data":data}
    return render(request, "Scheduler/Instructors.html", context)

def Admin_Login_View(request):
    
    form = LoginForm()
    context = {"form":form}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username , password = password)

        if user is not None:
            login(request,user)
            messages.info(request , 'Successfully Admin logged in')
            
            return redirect('Admin_Home')
        else:
            messages.warning(request , 'Something went wrong..')
            return redirect("Admin_Login")
    
    return render(request, "Scheduler/Admin_Login.html", context)



def Add_Course_View(request):
    form = Add_Course_Form()
    if request.method == "POST":
        print("mathod potsed")
        form = Add_Course_Form(request.POST)
        print("data posted")
        if form.is_valid():
            print("form is valid")
            form.save()
            messages.info(request , 'Course Added Succesfully!!')
            
            return redirect("Admin_Home")
        else:
            messages.warning(request , 'Something went wrong!!')
            print("form is invalid")


    context = {"form":form}
    return render(request,"Scheduler/Add_Course.html", context)

def Assign_Lecture_View(request):
    form = Assign_Lecture_Form()
    if request.method == "POST":
        print("mathod potsed")
        form = Assign_Lecture_Form(request.POST)
        print("data posted")
        if form.is_valid():
            form.save()
            messages.info(request , 'Lecture Assigned Succesfully!!')
            return redirect("Admin_Home")
        else:
            messages.warning(request , 'Something went wrong')
            print("form is invalid")


    context = {"form":form}
    return render(request,"Scheduler/Assign_Lecture.html",context)



def Instructor_Login_View(request):
    form = Instructor_Login_Form()
    if request.method == "POST":
        print("method posted")
        name = request.POST['name']
        password1 = request.POST['password1']

        user = authenticate(name = name , password1 = password1)
        
            

        if user is not None:
            login(request,user)
            messages.info(request , 'Instructor Logged in Succesfully!!')
            return redirect('Instructor_Home')
        else:
            
            return redirect("Instructor_Home")
    
    context = {"form":form}
    
    return render(request, "Scheduler/Instructor_Login.html",context)


def Add_Instructor_View(request):
    form = Add_Instructor_Form()
    if request.method == "POST":
        print("mathod potsed")
        form = Add_Instructor_Form(request.POST)
        print("data posted")
        if form.is_valid():
            print("form is valid")
            form.save()
            messages.info(request , 'Instructor added Succesfully!!')
            return redirect("Admin_Home")
        else:
            messages.warning(request , 'Something went wrong!!')
            return redirect("Instructors")
        
    context = {"form":form}
    return render(request,"Scheduler/Add_Instructor.html",context)


def Instructor_Home_View(request):
    data = Lectures.objects.all()
    context = {"data":data}
    return render(request,"Scheduler/Instructor_home.html",context)


def signout_view(request):
    logout(request)
    messages.warning(request , 'Successfully Logged off')
    
    return redirect('Home')
