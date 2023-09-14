from django.shortcuts import render

# Create your views here.
import datetime
dt=datetime.datetime.now()

def built_in_filter(request):
    d={'data': 'This is weak END','c':2,'dt':dt}
    return render(request,'built_in_filter.html',d)