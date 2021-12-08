from travello.models import Destinations
from django.shortcuts import render

# Create your views here.
def index(request):
    dests=Destinations.objects.all()
    return render(request,'index.html',{'dests':dests})