from hello.views import index
from django.urls import path
from . import views

#here dot means current directry
urlpatterns=[
    path("", views.index, name="index"),
    path("tinku", views.tinku, name="tinku"),
    path("<str:name>",views.greet,name="greet")
]