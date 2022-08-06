from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

class Cats:
    def __init__(self):
        self.cathead = "So cat's are dumb huh?"
        self.catbody = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit delectus voluptas sequi animi culpa, impedit, beatae quod optio minus saepe earum quos ut soluta magnam doloribus veniam quibusdam vero fuga."

def home(request):
    return render(request, 'search.html')

def result(request):
    print(request.GET)
    query = request.GET['q']
    cat = Cats()
    cat_list = [cat] * 4
    context = {'query': query, 'cat_list': cat_list}
    return render(request, 'result.html', context)

def update_view(request):
    return render(request, 'updatedb.html')

@csrf_exempt
def update_api(request):
    print(request.POST)
    return HttpResponse(200)