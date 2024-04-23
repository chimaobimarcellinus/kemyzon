from django.shortcuts import render
from django.http import HttpResponse
from.models import destination

# Create your views here.
def index(request):

    dest1 = destination()
    dest1.name = 'Nigeria'
    dest1.desc = 'The country that if so full of opportinuties'
    dest1.price = 900
    dest1.img = 'ban_img1.jpg'
    dest1.offer = False

    dest2 = destination()
    dest2.name = 'Canada'
    dest2.desc = 'the country that all citizen want to run to'
    dest2.price = 2000
    dest2.img = 'ban_img2.jpg'
    dest2.offer = True

    dest3 = destination()
    dest3.name = 'France Tower'
    dest3.desc = 'The city of psg team'
    dest3.price = 7000
    dest3.img = 'ban_img3.jpg'
    dest3.offer = False

    dests = [dest1, dest2, dest3]


    return render(request, 'index.html', {'dests': dests})