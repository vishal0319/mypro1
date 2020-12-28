from django.db import models
from django.db import connections
from django.forms import ModelForm
from django.contrib import admin

class Student(models.Model):
    Student_name= models.CharField(max_length=50)
    USN= models.CharField(max_length=10)
    Email_id= models.EmailField(max_length=20)
    Phone_number= models.IntegerField()
    Event_name= models.CharField(max_length=50)
    class Meta:
        db_table="student"
        
admin.site.register(Student)
class Volunteer(models.Model):
    Student_name=models.CharField(max_length=50)
    USN=models.CharField(max_length=15)
    In_time=models.TimeField(max_length=5)
    Out_time=models.TimeField(max_length=5)
    Event_name=models.CharField(max_length=50)
    Date=models.DateField(max_length=6)
    Attendance_status=models.CharField(max_length=20)
    class Meta:
        db_table="volunteer"

class Merchandise(models.Model):
    Student_name=models.CharField(max_length=50)
    USN=models.CharField(max_length=15)
    Size=models.CharField(max_length=10)
    Quantity=models.IntegerField() 
    Amount=models.IntegerField()
    class Meta:
        db_table="merchandise"
class expenditure(models.Model):
    date_time=models.DateTimeField()
    purpose=models.CharField(max_length=100)
    remarks=models.CharField(max_length=100)
    class Meta:
        db_table="expenditure"

# class studentform(ModelForm):
#     class Meta:
#         model = Student
#         fields = ['Student_name', 'USN', 'Email_id','Phone_number','Event_name']

# class volunteerform(ModelForm):
#     class Meta:
#         model = Volunteer
#         fields = ['Student_name', 'USN','In_time','Out_time','Event_name','Date','Attendance_status']

