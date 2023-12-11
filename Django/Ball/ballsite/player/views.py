from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify


menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

data_db = [
    { 'id': 1, 'title': 'Liverpool', 'content': 'About the Liverpool team', 'is_publish': True },
    { 'id': 2, 'title': 'Roma', 'content': 'About the Roma team', 'is publish': False },
    { 'id': 3, 'title': 'Newcastle', 'content': 'About the Newcastle', 'is_published': True},
    ]
def index(request):
    data = {'title': 'Football teams',
            'menu': menu,
            'posts': data_db,
            }
    return render(request, 'player/index.html', context=data)

def about(request):
    return render(request, 'player/about.html', {'title': 'О странице!'})

def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")

def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Categories to slug<h1><p>slug: {cat_slug}</p>")

def archive(request, year):
    if year > 2023:
        raise Http404()
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Сраница не найдена</h1>")


