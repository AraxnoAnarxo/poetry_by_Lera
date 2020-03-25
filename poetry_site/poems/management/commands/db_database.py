from django.core.management.base import BaseCommand
from poems.models import Poem
import re
#
# class Command(BaseCommand):
#     def handle(self, *args, **options):
# ________Добавление первой строки в объект базы данных________
#
#         poems = Poem.objects.all()
#         poems_all_str = []
#
#         first_str_list = []
#         for one_poem in poems:
#             text = one_poem.poem_text
#             str_list = text.split('\n')
#             poems_all_str.append(str_list)
#
#         for one_poem in poems_all_str:
#             if one_poem[0][-2] == '.' or one_poem[0][-2] == ',':
#                 one_poem[0] = one_poem[0][:-2]
#             q = Poem.objects.get(poem_text__startswith=one_poem[0])
#             q.first_line = one_poem[0]
#             q.save()
# ______________________

    #poems = Poem.objects.all()

# Всего:
        #print(len(poems))

# Запрос в базу без условия
#         for p in poems:
#             print(p.poem_title)

# Запрос в базу с условием
# get

       # poem = Poem.objects.get(poem_title = 'Человека')
       #
       #
       # print(poem)


# filter
#     poem = Poem.objects.filter(poem_title = '***')
# # Всего без названия:
#     print(len(poem))
#     for p in poem:
#         print(p.poem_title)

# first

    # poem = Poem.objects.first()
    # print(poem.poem_text)

# Добавление в базу данных
    ##Poem.objects.create(poem_text = '#', poem_name = '#')

# Delete
#     poem = Poem.objects.filter(poem_title = '#')
#     poem.delete()




# python manage.py shell
#from poems.models import Poem

