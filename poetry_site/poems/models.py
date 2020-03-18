from django.db import models

# Create your models here.


class Poem(models.Model):
    poem_title = models.CharField(max_length=100, default='***')
    poem_text = models.TextField()

    def __str__(self):
        return f'{self.poem_title}'




