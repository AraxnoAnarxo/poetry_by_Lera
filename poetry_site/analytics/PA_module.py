import string
# import collections
import pymorphy2
import random


# класс для одного стиха
class MetaPoet:
    def __init__(self, poem):
        self.poem = poem

    def __str__(self):
        return f'{self.poem}'

    def __len__(self):
        self.count = 0
        for x in self.poem:
            self.count += 1
        return self.count

    def remove_punctuation(self):
        for sign in string.punctuation:
            self.poem = self.poem.replace(sign, " ")
        return self.poem

    def split_words(self):
        self.poem = self.poem.split()
        return self.poem

    def lower_case(self):
        # words_of_poem = []
        self.poem = list(map(lambda word: word.lower(), self.poem))
        return self.poem

    def lemma(self):
        morph = pymorphy2.MorphAnalyzer()
        self.poem = list(map(lambda word: morph.parse(word)[0].normal_form, self.poem))
        return self.poem

    def unique_words(self):
        self.poem = set(self.poem)
        return self.poem


    def stop_words(self):
        pass

#
# if __name__ == '__main__':
#     # примеры
#     poem_1 = "Я помню! Чудное ; мгновенье, " \
#              "передо мной то явилась, ты -  я не  " \
#              "помню ничего кроме мгновенье"
#     poem_2 = 'Яблоко, упало на яблоко'
#
#     meta_poet_object = MetaPoet(poem_2)  # первоначальный текст
#     print(meta_poet_object)
#     print(len(meta_poet_object))  # выводит сколько всего символов
#
#     meta_poet_object.remove_punctuation()  # текст без пунктуации, знаки заменяет на пробел
#     print(meta_poet_object)
#     print(len(meta_poet_object))  # выводит сколько всего символов, но знаки заменяет на пробел
#
#     meta_poet_object.split_words()  # список слов
#     print(meta_poet_object)
#     print(len(meta_poet_object))  # выводит сколько всего слов
#
#     meta_poet_object.lower_case()  # слова с маленькой буквы
#     print(meta_poet_object)
#     print(len(meta_poet_object))  # выводит сколько всего слов
#
#     meta_poet_object.lemma()  # лемматизация
#     print(meta_poet_object)
#     print(len(meta_poet_object))  # выводит сколько всего слов
#
#     meta_poet_object.unique_words()  # уникальные слова
#     print(meta_poet_object)
#     print(len(meta_poet_object))


def generator(word_list):

    all_noun = []  # NOUN имя существительное хомяк
    all_adjf = []  # ADJF имя прилагательное (полное) хороший
    all_adjs = []  # ADJS имя прилагательное (краткое) хорош
    all_comp = []  # COMP компаратив лучше, получше, выше
    all_verb = []  # VERB глагол (личная форма) говорю, говорит, говорил
    all_infn = []  # INFN глагол (инфинитив) говорить, сказать
    all_prtf = []  # PRTF причастие (полное) прочитавший, прочитанная
    all_prts = []  # PRTS причастие (краткое) прочитана
    all_grnd = []  # GRND деепричастие прочитав, рассказывая
    all_numr = []  # NUMR числительное три, пятьдесят
    all_advb = []  # ADVB наречие круто
    all_npro = []  # NPRO местоимение-существительное он
    all_pred = []  # PRED предикатив некогда
    all_prep = []  # PREP предлог в
    all_conj = []  # CONJ союз и
    all_prcl = []  # PRCL частица бы, же, лишь
    all_intj = []  # INTJ междометие
    unknown_part = [] # не определенные pymorphy2 части речи

    morph = pymorphy2.MorphAnalyzer()

    for word in word_list:
        a = morph.parse(word)[0]
        if a.tag.POS == 'NOUN':
            all_noun.append(a.normal_form)
        elif a.tag.POS == 'ADJF':
            all_adjf.append(a.normal_form)
        elif a.tag.POS == 'ADJS':
            all_adjs.append(a.normal_form)
        elif a.tag.POS == 'COMP':
            all_comp.append(a.normal_form)
        elif a.tag.POS == 'VERB':
            all_verb.append(a.normal_form)
        elif a.tag.POS == 'INFN':
            all_infn.append(a.normal_form)
        elif a.tag.POS == 'PRTF':
            all_prtf.append(a.normal_form)
        elif a.tag.POS == 'PRTS':
            all_prts.append(a.normal_form)
        elif a.tag.POS == 'GRND':
            all_grnd.append(a.normal_form)
        elif a.tag.POS == 'NUMR':
            all_numr.append(a.normal_form)
        elif a.tag.POS == 'ADVB':
            all_advb.append(a.normal_form)
        elif a.tag.POS == 'NPRO':
            all_npro.append(a.normal_form)
        elif a.tag.POS == 'PRED':
            all_pred.append(a.normal_form)
        elif a.tag.POS == 'PREP':
            all_prep.append(a.normal_form)
        elif a.tag.POS == 'CONJ':
            all_conj.append(a.normal_form)
        elif a.tag.POS == 'PRCL':
            all_prcl.append(a.normal_form)
        elif a.tag.POS == 'INTJ':
            all_intj.append(a.normal_form)
        else:
            unknown_part.append(a)

    noun = random.choice(all_noun)
    all_noun.remove(noun)
    adjf = random.choice(all_adjf)
    infn = random.choice(all_infn)
    noun_inflect = random.choice(all_noun)
    all_noun.remove(noun_inflect)
    noun_end = random.choice(all_noun)


    p = morph.parse(noun)[0]
    # print(p.tag.gender, p.tag.number)
    q = morph.parse(infn)[0]

    # while q.tag.aspect == 'perf':
    #     all_infn.remove(infn)
    #     infn = random.choice(all_infn)
    while infn[-2:] == 'ся':
        all_infn.remove(infn)
        infn = random.choice(all_infn)
    # print(q.tag.aspect)
    print(infn)

    g = morph.parse(noun_inflect)[0]
    noun_inflected = g.inflect({'ablt'}).word

    z = morph.parse(noun_end)[0]
    noun_ended = z.inflect({'accs'}).word
# прилагательные
    # единственное число
    if p.tag.number == 'sing':
        # женский род
        if p.tag.gender == 'femn':
            if adjf[-3:] == 'кий':
                adjf = adjf[:-2] + 'ая'
            elif adjf[-2:] == 'ий':
                adjf = adjf[:-2] + 'яя'
            elif adjf[-2:] == 'ый':
                adjf = adjf[:-2] + 'ая'
            # исключения
            elif adjf[-1:] == 'ш':
                adjf = adjf + 'а'
            elif adjf[-3:] == 'тот':
                adjf = adjf[:-3] +'та'
            elif adjf == 'сам':
                adjf = 'сама'
            elif adjf == 'мой':
                adjf = 'моя'
            elif adjf == 'весь':
                adjf = 'вся'
        # средний род
        elif p.tag.gender == 'neut':
            if adjf[-3:] == 'кий':
                adjf = adjf[:-2] + 'ое'
            elif adjf[-2:] == 'ий':
                adjf = adjf[:-2] + 'ее'
            elif adjf[-2:] == 'ый':
                adjf = adjf[:-2] + 'ое'
            # исключения
            elif adjf == 'сам':
                adjf = 'само'
            elif adjf == 'мой':
                adjf = 'моё'
            elif adjf[-3:] == 'тот':
                adjf = adjf[:-3] +'то'
            elif adjf == 'весь':
                adjf = 'всё'
    # множественное число
    elif p.tag.number == 'plur':
        if adjf[-2:] == 'ий':
            adjf = adjf[:-2] + 'ие'
        elif adjf[-2:] == 'ый':
            adjf = adjf[-2:] + 'ые'
        elif adjf == 'мой':
            adjf = 'мои'
        elif adjf == 'весь':
            adjf = 'все'

# глаголы
    if infn == 'быть':
        infn = 'являет'
    elif infn == 'прийти':
        infn = 'приходит в'
    elif infn == 'избаловать':
        infn = 'избаловывет'
    # исключения
    elif infn == 'развить':
        infn = 'развивает'
    elif infn == 'пить':
        infn = 'пьёт'
    elif infn == 'петь':
        infn = 'поёт'
        noun_ended = z.inflect({'datv'}).word
    elif infn == 'вытекать':
        infn = 'вытекает ' + random.choice('в', 'через')
    elif infn == 'гнить':
        infn = 'гниёт'
        noun_inflected = g.inflect({'ablt'}).word
        noun_ended = z.inflect({'ablt'}).word
    elif infn == 'стать':
        infn = 'станет'
        noun_inflected = g.inflect({'gent'}).word
        noun_ended = z.inflect({'ablt'}).word
        # if q.tag.aspect == 'perf':
    #_______
    elif infn == 'забрать': # что сделать
        infn = 'забирает'

    elif infn == 'изрезать': # что сделать
        infn = 'изрезает'

    elif infn == 'растоптать':
        infn = 'растопчет'
    elif infn == 'размазать':
        infn = 'размажет'
    elif infn[-3:] == 'уть':
        infn = infn[:-3] + 'ет'
# _______

    elif infn[-3:] == 'ать':
        infn = infn[:-3] + 'ает'
    elif infn[-3:] == 'ить':
        infn = infn[:-3] + 'ит'
    elif infn[-3:] == 'еть':
        infn = infn[:-3] + 'ит'
    elif infn[-3:] == 'ыть':
        infn = infn[:-3] + 'оет'

    return f'{adjf.title()} {noun} {noun_inflected} {infn} {noun_ended}.'

