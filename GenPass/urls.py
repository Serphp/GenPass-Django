from django.urls import path
from . import views
from django.contrib.auth.models import User

urlpatterns = [
    path("", views.myfunctioncall, name="index"),
    path("gp", views.gp, name="gp"),
    ###### User
    path("registro/", views.registro, name="registro"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    ### Profiles
    path("profile/<str:username>/", views.profile, name="profile"),
    # path('<str:username>/', OtherProfileView.as_view(), name='other_profile'),
    ###
    path("servicios", views.servicios, name="servicios"),
    path("about", views.myfunctionabout, name="about"),
    ###
    path("add/<int:a>/<int:b>", views.add, name="add"),
    path("intro/<str:name>/<int:age>", views.intro, name="intro"),
    # path('myfirstpage',views.myfirstpage,name='myfirstpage'),
    # path("generate_password", views.generate_password, name="generate_password"),
]
