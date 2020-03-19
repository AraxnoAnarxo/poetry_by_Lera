from django.shortcuts import render
from django.http import HttpResponse
from .models import Poem

# Create your views here.
# перенесено в index.html (home_page)
def poems_all_(request):
    poems = Poem.objects.all()
    poems_all = []
    for one_poem in poems:
        text = one_poem.poem_text
        str_list = text.split('\n')
        poems_all.append(str_list)


    return render(request, 'poems/poems_all.html', {'poems':poems,'text':poems_all})
