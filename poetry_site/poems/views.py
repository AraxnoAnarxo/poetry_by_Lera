from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Poem

# Create your views here.
# перенесено в index.html (home_page)
def poems_all_(request):
    poems = Poem.objects.all()

    # poems_all = []
    # titles_all = []
    # for one_poem in poems:
    #     text = one_poem.poem_text
    #     title = one_poem.poem_title
    #     str_list = text.split('\n')
    #     titles_all.append(title)
    #     poems_all.append(str_list)
    #
    # zipped_list = zip(titles_all, poems_all)


    return render(request, 'poems/poems_all.html', {'poems':poems})

def poem_single(request, id):
    poem_single = get_object_or_404(Poem, id=id)
    return render(request, 'poems/poem_single.html', {'poem_single':poem_single})


