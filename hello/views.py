from django.shortcuts import render
from django.http import HttpResponse
from hello.models import Winery
from hello.forms import WineDescForm
from sklearn.externals import joblib
import csv


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
                winery = Winery()
                winery.latitude = row[1]
                winery.longitude = row[2]
                winery.winery = row[3]
                winery.province = row[4]
                winery.country = row[5]
                wineries.append(winery)
            except:
                pass
    context = {
        'wineries': wineries
    }
    return render(request, 'index.html', context)

def explore_data(request):
    return render(request, 'explore_data.html')

def predict(request):
    price_score = None
    qual_score = None
    if request.method == 'POST':
        form = WineDescForm(request.POST)
        if form.is_valid():
            price_model = joblib.load('./hello/data/wine_price_classifier.joblib.pkl')
            price_score = price_model.predict([form.cleaned_data['desc']])[0]
            qual_model = joblib.load('./hello/data/wine_qual_classifier.joblib.pkl')
            qual_score = qual_model.predict([form.cleaned_data['desc']])[0]
            price_score = price_score*20
            price_score = "$%d - $%d" %(price_score, price_score+19)
            qual_score = (qual_score*4) + 80
            qual_score = "%d - %d" %(qual_score, qual_score+3)
    else:
        form = WineDescForm()
    return render(request, 'predict.html', {'form': form, 'price_score': price_score, 'qual_score': qual_score})


