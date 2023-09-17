from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Adverts
from .forms import AdvertForm



# Create your views here.


def index(requests):
    adverts = Adverts.objects.all()
    context = {'adverts' : adverts}
    return render(requests, 'index.html', context)
    
    
def topSellers(request):
    return render(request, 'top-sellers.html')
    
def advertPost(request):
    if request.method == "POST":
        advert = AdvertForm(request.POST, request.FILES)
        print(advert)
        #if advert.is_valid():
        advertisement = Adverts(**advert.cleaned_data)
        advertisement.user = request.user
        advertisement.save()
        url = reverse('main-page')
        return redirect(url)
        #else: 
        #    print("advert.errors")

    else:
        advert = AdvertForm()
    content = {'advert' : advert}
    return render(request, 'advertisement-post.html', content)


def regis(request):
    return render(request, 'register.html')
    
def prof(request):
    return render(request, 'profile.html')
    
def log(request):
    return render(request, 'login.html')
    