from django.db import models
from datetime import datetime,date


class StaffList(models.Model):
    staffname= models.CharField(max_length=50)
    staffdob=models.DateField(blank=True, null=True)
    staffaddress= models.CharField(max_length=200,blank=True, null=True)
    staffemail= models.CharField(max_length=100,blank=True, null=True)
    staffphone=models.CharField(max_length=20,blank=True, null=True)
    staffcontract = models.CharField(max_length=20,blank=True, null=True)
    startdate=models.DateField(blank=True, null=True)
    termindate =models.DateField(blank=True, null=True)
    staffqual =models.CharField(max_length=250, blank=True,null=True)


  
    def __str__(self):
        return str(self.id) +  ' | '+ self.staffname +  ' | '+ str(self.staffdob)+ ' | '+ self.staffaddress+ ' | '+ self.staffemail+ ' | '+ self.staffphone+ ' | '+ self.staffcontract + ' | '+ str(self.startdate) + ' | ' + str(self.termindate) + ' | '+ self.staffqual

class TaskList(models.Model):

    taskdate=models.DateField(auto_now_add=False, auto_now=False)
    tasktime=models.TimeField(auto_now_add=False, auto_now=False,blank=True,null=True)
    taskdesc = models.CharField(max_length=200)
    location= models.CharField(max_length=50)
    assingees= models.ForeignKey(StaffList,blank=True,null=True,default="staff member deleted", on_delete=models.SET_DEFAULT)
    completed = models.BooleanField(default=False)
    comments=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return str(self.taskdate) + ' | ' + str(self.tasktime) + ' | ' +str(self.assingees) + ' | ' + self.taskdesc + ' | ' + str(self.location) + ' | ' +str(self.assingees) + ' | '  + str(self.completed)  + ' | '  + str(self.comments) 
