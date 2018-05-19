from django.shortcuts import render
from django.http import HttpResponse
from hello.models import Winery
import csv
import logging
from django.template import Context

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')

    #logger = logging.getLogger()

    wineries = []
    with open("./hello/data/winery_location 2.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                float(row[1])
                #print(row)
                winery = Winery()
                winery.latitude = row[1]
                winery.longitude = row[2]
                winery.winery = row[3]
                winery.province = row[4]
                winery.country = row[5]
                #winery.save()
                wineries.append(winery)
            except:
                pass
    context = {
        'wineries': wineries
    }
    return render(request, 'index.html', context)

def explore_data(request):
    return render(request, 'explore_data.html')
