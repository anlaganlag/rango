from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=1314)
    likes = models.IntegerField(default=520)
    
    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=8)
    def __str__(self):
        return self.title
