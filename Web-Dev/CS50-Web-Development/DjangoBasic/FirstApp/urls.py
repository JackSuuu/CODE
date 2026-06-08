from django.urls import path
from . import views

urlpatterns = [
    # The first route represent the origin link of the app
    # For example: http://127.0.0.1:8000/FirstApp/
    path("", views.index, name="index"),
    # This route can be any string that you can given a name to
    # For example: if the link is http://127.0.0.1:8000/FirstApp/Harry
    # It will display Hello, Harry instead
    path("<str:name>", views.greet, name="greet"),
    path("jack", views.jack, name="jack"),
    path("leo", views.leo, name="Leo")
]

