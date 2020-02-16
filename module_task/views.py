from django.shortcuts import render,redirect
from .models import TaskList,StaffList
from .forms import TaskListForm,StaffListForm

from django.contrib import messages
from django.http import HttpResponseRedirect


############### DASHBOARD/HOME/WEATHER API #########################################################################
##  https://developer.accuweather.com/
##  This weather API is for a trial account and is limited to 50 calls/day, more than this will result in no data



def index(request):
    import json
    import requests
  
  ## Uncomment next line for api request - disabled during development to prevent multiple calls
  
    ##api_request = requests.get("http://dataservice.accuweather.com/forecasts/v1/daily/1day/1079064?apikey=kmrDSxJckPLxThWvCAlCGsk3ZRhbCimd%20&language=en-us&details=true&metric=true")
    

    try:
        api = json.loads(api_request.content)

    except Exception as e:
        api = "Weather API Error"

    return render(request,'index.html',{'api':api}) 

############### TASKS ##################################################################################

#function display task module and to post new tasks to database table
def task(request):

    if request.method == 'POST':
        form = TaskListForm(request.POST or None)

        #save task and return success message
        #if form.isvalid():
        form.save()
        all_tasks = TaskList.objects.all
        messages.success(request, ('Task has been successfully added!'))
        return render(request,'task.html',{'all_tasks': all_tasks})

    else:   
        all_tasks = TaskList.objects.all
        return render(request,'task.html',{'all_tasks': all_tasks})


#function to delete a single task with success message
def delete(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    messages.success(request, ('Task has been successfully deleted!'))
    return redirect('task')

#function to flag tasks as complete
def markcomplete(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.completed= True
    task.save()
    return redirect('task')

#function to flag tasks as not complete
def markincomplete(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.completed= False
    task.completedby=('')
    task.save()
    return redirect('task')

#function to edit tasks
def edittask(request, task_id):
    if request.method == 'POST':
        task = TaskList.objects.get(pk=task_id)
        form = TaskListForm(request.POST or None, instance=task)
        

        #save task and return success message
       # if form.isvalid():
        form.save()
        messages.success(request, ('Task has been modified!'))
        return redirect('task')

    else:   
        task = TaskList.objects.get(pk=task_id)
      
        return render(request,'edittask.html' ,{'task': task})


####################  CUSTOMERS   ########################################
def people(request):
    return render(request,'people.html',{})


####################  STAFF   ########################################
def staff(request):
    if request.method == 'POST':
        form = StaffListForm(request.POST or None)

        #save task and return success message
        #if form.isvalid():
        form.save()
        all_staff = StaffList.objects.all
        messages.success(request, ('Staff member has been successfully added!'))
        return render(request,'staff.html',{'all_staff': all_staff})

    else:   
         all_staff = StaffList.objects.all
         return render(request,'staff.html',{'all_staff': all_staff})


#function to delete a single staff member with success message
def deletestaff(request, staff_id):
    staff = StaffList.objects.get(pk=staff_id)
    staff.delete()
    messages.success(request, ('Staff member has been successfully deleted!'))
    return redirect('staff')


#function to edit staff member
def editstaff(request, staff_id):
    if request.method == 'POST':
        staff = StaffList.objects.get(pk=staff_id)
        form = StaffListForm(request.POST or None, instance=staff)

        #save staff member and return success message
        # if form.isvalid():
        form.save()
        messages.success(request, ('Staff member has been modified!'))
        return redirect('staff')

    else:   
        staff = StaffList.objects.get(pk=staff_id)
        return render(request,'editstaff.html',{'staff': staff})

 ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

def horses(request):
    return render(request,'horses.html',{})

def rota(request):
    return render(request,'rota.html',{})

def lessons(request):
    return render(request,'lessons.html',{})

 