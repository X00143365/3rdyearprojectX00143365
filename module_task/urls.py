
from django.urls import path
from . import views



urlpatterns = [ 
    
    path('',views.index, name='index'),
    path('people',views.people, name='people'),
    path('task',views.task, name='task'),
    path('horses',views.horses, name='horses'),
    path('staff',views.staff, name='staff'),
    path('rota',views.rota, name='rota'),
    path('rotaview',views.rotaview, name='rotaview'),
    path('lessons',views.lessons, name='lessons'),
    path('delete/<task_id>', views.delete, name ='delete'),
    path('delallcomplete', views.delallcomplete, name ='delallcomplete'),
    path('deletestaff/<staff_id>', views.deletestaff, name ='deletestaff'),
    path('deleterota/<rota_id>', views.deleterota, name ='deleterota'),
    path('markcomplete/<task_id>', views.markcomplete, name='markcomplete'),   
    path('markincomplete/<task_id>', views.markincomplete, name='markincomplete'),
    path('edittask/<task_id>', views.edittask, name='edittask'),  
    path('editstaff/<staff_id>', views.editstaff, name='editstaff'),
    path('editrota/<rota_id>', views.editrota, name='editrota'),
    
]
