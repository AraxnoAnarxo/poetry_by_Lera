from django.db import models

# Create your models here.


class Poem(models.Model):
    poem_title = models.CharField(max_length=100, default='***', null=True)
    poem_text = models.TextField(null=True)
    first_line = models.TextField(default=poem_title, null=True)

    def __str__(self):
        return f'{self.poem_text}'




