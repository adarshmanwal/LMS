
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("upload", views.Admin, name= "admin"),
    path("update/<int:id>", views.update , name= "admin"),
    path("delete/<int:id>", views.delete , name= "admin"),
]
