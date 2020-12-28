from django.shortcuts import render
from mypro.models import Student
from django.contrib import messages
from mypro.models import Volunteer
from mypro.models import Merchandise
from mypro.models import expenditure
#from mypro.models import studentform
#from mypro.models import volunteerform

def homepage(request):
    return render(request,'home.html')

def stdrecord(request):
    if request.method=="POST":
        if request.POST.get('Student_name') and request.POST.get('USN') and request.POST.get('Email_id') and request.POST.get('Phone_number') and request.POST['Event_name']:
            saverecord=Student()
            saverecord.Student_name= request.POST.get('Student_name')
            saverecord.USN= request.POST.get('USN')
            saverecord.Email_id= request.POST.get('Email_id')
            saverecord.Phone_number= request.POST.get('Phone_number')
            saverecord.Event_name= request.POST['Event_name']
            saverecord.save()
            messages.success(request,'registration successfull')
            return render(request,'Std_form.html')
        else:
            messages.error(request,'incorrect data')
            print('invalid')
            return render(request,'Std_form.html')
    else:
            return render(request,'Std_form.html')

def volrecord(request):
    if request.method=="POST":

        if request.POST.get('Student_name') and request.POST.get('USN') and request.POST.get('In_time') and request.POST.get('Out_time') and request.POST['Event_name'] and request.POST['Date'] and request.POST['Attendance_status']:
            saverecord=Volunteer()
            saverecord.Student_name= request.POST.get('Student_name')
            saverecord.USN= request.POST.get('USN')
            saverecord.In_time= request.POST.get('In_time')
            saverecord.Out_time= request.POST.get('Out_time')
            saverecord.Event_name= request.POST['Event_name']
            saverecord.Date= request.POST['Date']
            saverecord.Attendance_status= request.POST['Attendance_status']
            saverecord.save()
            messages.success(request,'registration successfull')
            print('succesfully saved')
            return render(request,'Vol_form.html')
        else:
            messages.error(request,'incorrect data')
            print('invalid')
            return render(request,'Vol_form.html')
            
    else:
            return render(request,'Vol_form.html')

def mrecord(request):
    if request.method=="POST":

        if request.POST.get('Student_name') and request.POST.get('USN') and request.POST.get('Size') and request.POST.get('Quantity') and request.POST.get('Amount'):
            saverecord=Merchandise()
            saverecord.Student_name= request.POST.get('Student_name')
            saverecord.USN= request.POST.get('USN')
            saverecord.Size= request.POST.get('Size')
            saverecord.Quantity= request.POST.get('Quantity')
            saverecord.Amount= request.POST.get('Amount')
            saverecord.save()
            messages.success(request,'registration successfull')
            print('succesfully saved')
            return render(request,'mform.html')
        else:
            messages.error(request,'incorrect data')
            print('invalid')
            return render(request,'mform.html')
            
    else:
            return render(request,'mform.html')

def exprecord(request):
    if request.method=="POST":

        if request.POST.get('date_time') and request.POST.get('purpose') and request.POST.get('remarks'): 
            saverecord=expenditure()
            saverecord.date_time= request.POST.get('date_time')
            saverecord.purpose= request.POST.get('purpose')
            saverecord.remarks= request.POST.get('remarks')
            saverecord.save()
            messages.success(request,'registration successfull')
            print('succesfully saved')
            return render(request,'Vol_form.html')
        else:
            messages.error(request,'incorrect data')
            print('invalid')
            return render(request,'expform.html')
            
    else:
            return render(request,'expform.html')
# def home_view(request): 
#     context ={} 
  
#     # create object of form 
#     form = studentform(request.POST or None, request.FILES or None) 
      
#     # check if form data is valid 
#     if form.is_valid(): 
#         # save the form data to model 
#         form.save() 
  
#     context['form']= form 
#     return render(request, "home.html", context) 
