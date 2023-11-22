from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from django.template.loader import render_to_string

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

def index(request):
    # t = render_to_string('player/index.html')
    # return HttpResponse(t)
    data = {'title': 'Главная страница!!!',
            'menu': menu,
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


