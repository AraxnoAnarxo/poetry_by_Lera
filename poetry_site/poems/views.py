from django.shortcuts import render
from django.http import HttpResponse
from .models import Poem

# Create your views here.
# перенесено в index.html (home_page)
# def poems_all(request):
#     poems = Poem.objects.all()
#
#     return render(request, 'poems/index.html', {'poems':poems})
