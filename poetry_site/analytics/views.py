from django.shortcuts import render
from poems.models import Poem
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
import collections, pymorphy2

# Create your views here.

from .PA_module import MetaPoet # написала модуль для анализа стихов: подсчет слов + top 100 слов

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
    #         all_noun = []  # NOUN имя существительное хомяк]
    #         all_noun = []  # NOUN имя существительное хомяк
    #         all_adjf = []  # ADJF имя прилагательное (полное) хороший
    #         all_adjs = []  # ADJS имя прилагательное (краткое) хорош
    #         all_comp = []  # COMP компаратив лучше, получше, выше
    #         all_verb = []  # VERB глагол (личная форма) говорю, говорит, говорил
    #         all_infn = []  # INFN глагол (инфинитив) говорить, сказать
    #         all_prtf = []  # PRTF причастие (полное) прочитавший, прочитанная
    #         all_prts = []  # PRTS причастие (краткое) прочитана
    #         all_grnd = []  # GRND деепричастие прочитав, рассказывая
    #         all_numr = []  # NUMR числительное три, пятьдесят
    #         all_advb = []  # ADVB наречие круто
    #         all_npro = []  # NPRO местоимение-существительное он
    #         all_pred = []  # PRED предикатив некогда
    #         all_prep = []  # PREP предлог в
    #         all_conj = []  # CONJ союз и
    #         all_prcl = []  # PRCL частица бы, же, лишь
    #         all_intj = []  # INTJ междометие

    c = collections.Counter(lemmed_words)
    result = c.most_common(100)

    return render(request, 'analytics/counter_top_100.html', {'result':result,'counter_all': counter_all,'counter_unique':counter_unique})#,unique_words_list':unique_words_list})

# реализовать аналитику по частям речи
#
#         for word in all_words_initially_lemmed:
#             a = morph.parse(word)[0]
#             if a.tag.POS == 'NOUN':
#                 all_noun.append(a.normal_form)
#             elif a.tag.POS == 'ADJF':
#                 all_adjf.append(a.normal_form)
#             elif a.tag.POS == 'ADJS':
#                 all_adjs.append(a.normal_form)
#             elif a.tag.POS == 'COMP':
#                 all_comp.append(a.normal_form)
#             elif a.tag.POS == 'VERB':
#                 all_verb.append(a.normal_form)
#             elif a.tag.POS == 'INFN':
#                 all_infn.append(a.normal_form)
#             elif a.tag.POS == 'PRTF':
#                 all_prtf.append(a.normal_form)
#             elif a.tag.POS == 'PRTS':
#                 all_prts.append(a.normal_form)
#             elif a.tag.POS == 'GRND':
#                 all_grnd.append(a.normal_form)
#             elif a.tag.POS == 'NUMR':
#                 all_numr.append(a.normal_form)
#             elif a.tag.POS == 'ADVB':
#                 all_advb.append(a.normal_form)
#             elif a.tag.POS == 'NPRO':
#                 all_npro.append(a.normal_form)
#             elif a.tag.POS == 'PRED':
#                 all_pred.append(a.normal_form)
#             elif a.tag.POS == 'PREP':
#                 all_prep.append(a.normal_form)
#             elif a.tag.POS == 'CONJ':
#                 all_conj.append(a.normal_form)
#             elif a.tag.POS == 'PRCL':
#                 all_prcl.append(a.normal_form)
#             elif a.tag.POS == 'INTJ':
#                 all_intj.append(a.normal_form)
#             else:
#                 unknown_part.append(a)
#
#
#         parts_of_speech_len_dict = {
#             'len_all_noun': len(all_noun),
#             'len_all_adjf': len(all_adjf),
#             'len_all_adjs': len(all_adjs),
#             'len_all_comp': len(all_comp),
#             'len_all_verb': len(all_verb),
#             'len_all_infn': len(all_infn),
#             'len_all_prtf': len(all_prtf),
#             'len_all_prts': len(all_prts),
#             'len_all_grnd': len(all_grnd),
#             'len_all_numr': len(all_numr),
#             'len_all_advb': len(all_advb),
#             'len_all_npro': len(all_npro),
#             'len_all_pred': len(all_pred),
#             'len_all_prep': len(all_prep),
#             'len_all_conj': len(all_conj),
#             'len_all_prcl': len(all_prcl),
#             'len_all_intj': len(all_intj),
#             'unknown_part': len(unknown_part),
#              }
#         return render(request, 'analytics/parts_of_speech.html', {'parts_of_speech_len_dict':parts_of_speech_len_dict})
#