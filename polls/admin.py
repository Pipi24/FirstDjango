from django.contrib import admin
from polls import models

# Register your models here.


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date']


admin.site.register(models.BookInfo, BookInfoAdmin)
admin.site.register(models.HeroInfo)
