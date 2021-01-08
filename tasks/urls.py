from hello.views import index
from django.urls import path
from . import views
app_name="tasks"
urlpatterns=[
    path('',views.index,name='task_index'),
    path('add',views.add,name="add")
]