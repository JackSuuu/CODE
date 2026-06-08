from django.urls import path
from . import views

# This is how we use as a variable in Django HTML
# For example: we name tasks:index to redirect the link back
app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add")
]
