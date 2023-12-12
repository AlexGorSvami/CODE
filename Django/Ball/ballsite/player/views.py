from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

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

def show_post(request, post_id):
    return HttpResponse(f'Show article with id = {post_id}')

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Сраница не найдена</h1>")

def addpage(request):
    return HttpResponse(f'Add page')

def contact(request):
    return HttpResponse(f'Feedback')

def login(request):
    return HttpResponse(f'Authorization')


