from django.core.management.base import BaseCommand
from poems.models import Poem

class Command(BaseCommand):
    def handle(self, *args, **options):
        #poems = Poem.objects.all()

# Всего:
        #print(len(poems))

# Запрос в базу без условия
#         for p in poems:
#             print(p.poem_title)

# Запрос в базу с условием
# get

       poem = Poem.objects.get(poem_title = 'Человека')


       print(poem)

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

