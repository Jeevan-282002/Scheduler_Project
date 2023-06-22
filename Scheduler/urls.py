from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home_View, name = "Home"),
    path("Instructor_Home/", views.Instructor_Home_View, name = "Instructor_Home"),
    path("Admin_Home/", views.Admin_Home_View, name = "Admin_Home"),
    path("Instructors/", views.Instructors_View, name = "Instructors"),
    path("Admin_Login/", views.Admin_Login_View, name = "Admin_Login"),
    path("Add_Course/", views.Add_Course_View, name = "Add_Course"),
    path("Add_Instructor/", views.Add_Instructor_View, name = "Add_Instructor"),
    path("Assign_Lecture/", views.Assign_Lecture_View, name = "Assign_Lecture"),
    path("Instructor_Login/", views.Instructor_Login_View, name = "Instructor_Login"),
    path('signout/',views.signout_view , name = 'signout'),
]