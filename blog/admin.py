from django.contrib import admin
from .models import *
from . import *
# Register your models here.


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)