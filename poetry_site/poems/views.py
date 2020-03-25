from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Poem
from .forms import PoemForm
from functools import reduce


# главная страница
def home_page(request):
    return render(request, 'poems/index.html')


# Create your views here.
# Автоматическая генерация view

class Poems_All_ListView(ListView):
    model = Poem
    template_name = 'poems/poems.html'
    context_object_name = 'poems'


class PoemListView(ListView):
    model = Poem
    template_name = 'poems/content.html'
    context_object_name = 'poems'

#
# def poems_all_(request):
#
#
#
#     poems = Poem.objects.all()
#     poems_all_str = []
#
#     first_str_list = []
#     titles_all =[]
#     for one_poem in poems:
#         text = one_poem.poem_text
#         str_list = text.split('\n')
#         poems_all_str.append(str_list)
#
#         title = one_poem.poem_title
#         titles_all.append(title)
#     for one_poem in poems_all_str:
#         if one_poem[0][-2] == '.' or one_poem[0][-2] == ',':
#             one_poem[0] = one_poem[0][:-2]
#         first_str_list.append(one_poem[0])
#
#     zipped_list = zip(titles_all, first_str_list)
#
#     # poems_all = []
#     # titles_all = []
#     # for one_poem in poems:
#     #     text = one_poem.poem_text
#     #     title = one_poem.poem_title
#     #     str_list = text.split('\n')
#     #     titles_all.append(title)
#     #     poems_all.append(str_list)
#     #
#     # zipped_list = zip(titles_all, poems_all)
#     return render(request, 'poems/poems_all.html',{'zipped_list':zipped_list})

    # return render(request, 'poems/poems_all.html', {'poems':first_str_list})

def poem_single(request, id):
    poem_single = get_object_or_404(Poem, id=id)
    return render(request, 'poems/poem_single.html', {'poem':poem_single})

def poem_add(request):
    if request.method == 'GET':
        form = PoemForm()
        return render(request, 'poems/poem_add.html', {'form':form})
    else:
        form = PoemForm(request.POST)
        if form.is_valid():
            # обработка данных

            form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'poems/poem_add.html', {'form': form})






