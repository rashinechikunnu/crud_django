from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name='home'),
    path("list",views.list,name='list'),
    path("edit/<pk>",views.edited,name='edit'),
    path("delete/<pk>",views.delete,name='delete')
    
]
