import csv
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    data = []
    with open(BUS_STATION_CSV, 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(data, 15)
    page = paginator.get_page(page_number)
    bus_stations = [elem for elem in page]
    context = {
        'bus_stations': bus_stations,
        'page': page
    }
    return render(request, 'stations/index.html', context)


