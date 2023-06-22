from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    password1 = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Courses(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images", blank=True)
    batch = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.level} - {self.name}"
        
    def clean(self):
        if  Courses.objects.filter(batch = self.batch, name = self.name, level = self.level).exists():
            raise ValidationError('The batch already present')
            
    
class Lectures(models.Model):
    date = models.DateField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.date} - {self.course} - {self.instructor}"
    
    def clean(self):
        if Lectures.objects.filter(date=self.date, instructor=self.instructor).exists():
            raise ValidationError('The instructor is already assigned to a lecture on this date.')
        
    
    
    