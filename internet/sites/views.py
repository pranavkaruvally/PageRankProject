from django.shortcuts import render

# Create your views here.
def health_view(request, site_id):
    file_name = 'health/' + site_id + ".html"
    return render(request, file_name)

def technology_view(request, site_id):
    file_name = 'technology/' + site_id + ".html"
    return render(request, file_name)

def cars_view(request, site_id):
    file_name = 'cars/' + site_id + ".html"
    return render(request, file_name)

def animals_view(request, site_id):
    file_name = 'animals/' + site_id + ".html"
    return render(request, file_name)

def business_view(request, site_id):
    file_name = 'business/' + site_id + ".html"
    return render(request, file_name)

def movies_view(request, site_id):
    file_name = 'movies/' + site_id + ".html"
    return render(request, file_name)