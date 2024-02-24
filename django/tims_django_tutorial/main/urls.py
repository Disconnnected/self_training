from  django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("view1", views.view_1, name = "view_1"),
    path("view2", views.view_2, name = "view_2")
]