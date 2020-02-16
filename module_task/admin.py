from django.contrib import admin

from .models import TaskList
from .models import StaffList


admin.site.register(TaskList)
admin.site.register(StaffList)
