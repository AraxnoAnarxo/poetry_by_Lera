from django.shortcuts import render
from django.http import HttpResponse
from poems.models import Poem

# Create your views here.

def poems_all(request):
    poems = Poem.objects.all()
    poems_all = []
    titles_all = []
    for one_poem in poems:
        text = one_poem.poem_text
        title = one_poem.poem_title
        text = text.split('\n')
        poems_all.append(text)
        titles_all.append(title)

    zipped_list = zip(titles_all, poems_all)


    return render(request, 'poems/index.html', {'poems':zipped_list})

# def poems_all(request):
#     poems = Poem.objects.all()
#     # for one_poem in poems:
#     #     text = one_poem.poem_text
#     #     text = text.split('\n')
#     return render(request, 'poems/index.html', {'poems':poems})

# Create your views here.

# def home_page(request):
#     return render(request, 'poems/index.html')
