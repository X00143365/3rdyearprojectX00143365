from django.contrib import admin

from .models import TaskList
from .models import StaffList
from .models import RotaList


admin.site.register(TaskList)
admin.site.register(StaffList)
admin.site.register(RotaList)
