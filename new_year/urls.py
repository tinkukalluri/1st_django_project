from hello.views import index
from django.urls import path
from new_year import views

urlpatterns =[

    path("",views.index,name="new_year")
]

