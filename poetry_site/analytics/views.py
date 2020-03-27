from django.shortcuts import render
from poems.models import Poem
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
import collections, pymorphy2

# Create your views here.

from .PA_module import MetaPoet, generator # написала модуль для анализа стихов: подсчет слов + top 100 слов

# функции для отображения на сайте
# общая страница аналитики (без переменных)
def form_analytics(request):
    return render(request, 'analytics/poems_analytics.html')
# подсчет числа слов всего, уникальных слов, топ 100 слов
def all_words_counted(request):
    poems = Poem.objects.all() # все объекты класса Стихи
    unique_words_list = []
    lemmed_words = []
    counter_all = 0
    counter_unique = 0
    for poem in poems:
        poem = str(poem.poem_text)
        meta_poem = MetaPoet(poem) # создаем объект класса MetaPoet, куда передаем стихи
        meta_poem.remove_punctuation()
        meta_poem.split_words()
        counter_all += len(meta_poem)
        meta_poem.lower_case()
        lemmed_words += meta_poem.lemma()
        meta_poem.unique_words()
        counter_unique += len(meta_poem)


    morph = pymorphy2.MorphAnalyzer()
    # список топ 100 из существительных и глаголов
    lemmed_words = [word for word in lemmed_words if morph.parse(word)[0].tag.POS == 'NOUN' or morph.parse(word)[0].tag.POS == 'INFN']


    c = collections.Counter(lemmed_words)
    result = c.most_common(100)


    return render(request, 'analytics/counter_top_100.html', {'result':result,'counter_all': counter_all,'counter_unique':counter_unique})#,unique_words_list':unique_words_list})

def view_generator(request):
    return render(request, 'analytics/phrase_generator.html')


def phrase_generator(request):
    poems = Poem.objects.all() # все объекты класса Стихи
    unique_words_list = []
    lemmed_words = []
    for poem in poems:
        poem = str(poem.poem_text)
        meta_poem = MetaPoet(poem) # создаем объект класса MetaPoet, куда передаем стихи
        meta_poem.remove_punctuation()
        meta_poem.split_words()
        meta_poem.lower_case()
        meta_poem.lemma()
        word_set = meta_poem.unique_words()

    phrase = generator(word_set)



    return render(request, 'analytics/phrase.html', {'phrase':phrase})

