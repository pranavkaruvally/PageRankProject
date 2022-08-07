from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from server.models import Website
import json
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

# Create your views here.

# class Cats:
#     def __init__(self):
#         self.cathead = "So cat's are dumb huh?"
#         self.catbody = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit delectus voluptas sequi animi culpa, impedit, beatae quod optio minus saepe earum quos ut soluta magnam doloribus veniam quibusdam vero fuga."

def home(request):
    return render(request, 'search.html')

def result(request):
    print(request.GET)
    query = request.GET['q']
    # cat = Cats()
    # cat_list = [cat] * 4
    # context = {'query': query, 'cat_list': cat_list}

    websites = Website.objects.all()
    context = {'query': query, 'websites': websites}

    return render(request, 'result.html', context)

def update_view(request):
    return render(request, 'updatedb.html')

def scrape_url(url):
    url = url.strip()
    print(url)
    req = Request(url)
    html_doc = urlopen(req)
	
    soup = BeautifulSoup(html_doc, "lxml")
    sample_content = ' '.join(soup.p.string.strip().split())
    title = soup.h1.string.strip()
	
    return title, sample_content

@csrf_exempt
def update_api(request):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    urls = body["URLs"]

    for url in urls:
        all_objects = Website.objects.all().filter(url=url)
        if all_objects:
            continue
        title, sample_content = scrape_url(url)
        page = Website(url=url, title=title, sample_content=sample_content)
        page.save()

    return HttpResponse(200)