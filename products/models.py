from django.db import models

class Game(models.Model):
    title=models.CharField(max_length=100)
    company=models.TextField()
    price=models.FloatField()


# genre,owner,image,characters,характеристики(eng),mb more~~
