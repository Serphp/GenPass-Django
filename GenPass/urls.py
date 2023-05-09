from django.urls import path
from . import views

urlpatterns = [
    path("", views.myfunctioncall, name="index"),
    path("gp", views.gp, name="gp"),
    ######
    path("about", views.myfunctionabout, name="about"),
    path("add/<int:a>/<int:b>", views.add, name="add"),
    path("intro/<str:name>/<int:age>", views.intro, name="intro"),
    # path('myfirstpage',views.myfirstpage,name='myfirstpage'),
    # path("generate_password", views.generate_password, name="generate_password"),
    path("myimagepage5/<str:imagename>", views.myimagepage5, name="myimagepage5"),
    path("myform", views.myform, name="myform"),
    path("submitmyform", views.submitmyform, name="submitmyform"),
    path("myform2", views.myform2, name="myform2"),
]
