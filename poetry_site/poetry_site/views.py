from django.shortcuts import render
from django.http import HttpResponse
from poems.models import Poem

# Create your views here.

def poems_all(request):
    poems = Poem.objects.all()
    return render(request, 'poems/index.html', {'poems':poems})


# Create your views here.

# def home_page(request):
#     return render(request, 'poems/index.html')
