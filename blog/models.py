from django.db import models
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    title =models.CharField('Nomi', max_length=255)
    date = models.DateTimeField('Sana', default=timezone.now)
    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
        

class Post(models.Model):
    title = models.CharField('Sarlavhasi',max_length=255)
    content = models.TextField('matn')
    categories = models.ForeignKey(Category, on_delete = models.CASCADE, null=True)
    image = models.ImageField('Rasm', blank=True, null=True)
    date = models.DateTimeField('Sana', default=timezone.now)
    publish = models.BooleanField('ekranga chiqish', default=False)
    views = models.IntegerField("ko'rilganlar",default=0)

    class Meta: 
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    author_name = models.CharField('Foydalanuvchi', max_length = 50)
    text = models.TextField('Kommentariya', max_length=1000)


    class Meta:
        verbose_name = 'Kommentariya'
        verbose_name_plural = 'Kommentariyalar'

