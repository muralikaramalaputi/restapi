from django.urls import path
from .views import *

urlpatterns =[
    path('retrieve/',retrieve,name="retrieve"),
    path('create/',create,name="create"),
    path('update/<int:id>/',update,name="update"),
    path('delete/<int:id>/',delete,name="delete"),
    
]
