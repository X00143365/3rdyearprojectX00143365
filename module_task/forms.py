from django import forms
from django.forms import ModelChoiceField
from .models import TaskList
from .models import StaffList

class TaskListForm (forms.ModelForm):
   
    class Meta:
        model = TaskList
        fields = ["taskdate", "tasktime","taskdesc","location","assingees","comments","completed"]


class StaffListForm (forms.ModelForm):
    class Meta:
        model = StaffList
        fields = ["staffname","staffdob","staffaddress","staffemail","staffphone","staffcontract","startdate","termindate","staffqual"]
       




