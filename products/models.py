from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    title=models.CharField(max_length=100)
    company=models.TextField()
    price=models.FloatField()
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(blank=True,null=True)
    slug=models.SlugField(blank=True,null=True)
    def __str__(self):
        return f'{self.title} - {self.company}'

        
# genre,owner,image,characters,характеристики(eng),mb more~~
# git commit -m"Updated Model/Created Genre"

# git add -A
# git commit -m""
# git push