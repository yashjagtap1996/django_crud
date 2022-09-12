from django.urls import path
from sampleapp import views

urlpatterns=[
    path("",views.crud,name='home'),
    path("delete/<int:id>/",views.delete,name='delete'),
    path("update/<int:id>/",views.update,name="update")
]