from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from . models import Courses, Lectures, Instructor

class LoginForm(AuthenticationForm):

    username = forms.CharField(label='Enter Your Username' , widget=forms.TextInput(attrs={'class':'form-control'}))

    password = forms.CharField(label='Enter Your Password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User

batch_choice = [("10AM to 12PM", '10AM to 12PM'), ("1PM to 3PM", '1PM to 3PM'), ("4PM to 6PM",'4PM to 6PM')]



level_choice = [("Core",'Core'),("Advance",'Advance')]

class Add_Course_Form(forms.ModelForm):

    batch = forms.ChoiceField(choices=batch_choice, label='Select Batch', 
    widget=forms.Select(attrs={'class':'form-control'}))

    level = forms.ChoiceField(choices=level_choice, label='Select Level', 
    widget=forms.Select(attrs={'class':'form-control'}))

    class  Meta:
        model = Courses
        fields = ["name","level","description","image","batch"]

        labels = {
            "name":"Enter Course Name",
            "description":"Enter Description",
            "image":"Enter Image",
            "batch":"Enter Batch",
        }

        widgets = {
            
            "name": forms.TextInput(attrs={'class':'form-control'}),
            "level": forms.TextInput(attrs={'class':'form-control'}),
            "description": forms.Textarea(attrs={'class':'form-control','rows':'5','cols':'10'}),
            "image": forms.FileInput(attrs={'class':'form-control'}),
            
        }


class Assign_Lecture_Form(forms.ModelForm):
    class Meta:
        model = Lectures
        fields = ["date","course","instructor"]

        labels = {
            "date":"Select Date",
            "course":"Select Course",
            "instructor":"Select Instructor"

        }
        
class Instructor_Login_Form(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ["name","password1"]
        labels = {

            "name":"Enter Name",
            "password1":"Enter Password",
            
        }

        widgets = {
            
            "name": forms.TextInput(attrs={'class':'form-control'}),
            "password1": forms.PasswordInput(attrs={'class':'form-control'}),
            
        }



class Add_Instructor_Form(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ["name","password1"]
        labels = {

            "name":"Enter Name",
            "password1":"Enter Password",
            
        }

        widgets = {
            
            "name": forms.TextInput(attrs={'class':'form-control'}),
            "password1": forms.PasswordInput(attrs={'class':'form-control'}),
            
        }
        