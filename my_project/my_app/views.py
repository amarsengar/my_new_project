from django.shortcuts import render
from my_app.models import MyModels
import os

# Create your views here.


def my_view(request):
    
    terminal = os.system("start cmd /K dir")
    # terminal =os.system("gnome-terminal -e 'bash -c \"sudo apt-get update; exec bash\"'")
    

    return render(request,template_name='index.html')