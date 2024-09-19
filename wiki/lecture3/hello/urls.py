from django.urls import path

#from . punto o dot quiere decir del directorio actual , importa views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("brian",views.brian, name="brian")
    ]