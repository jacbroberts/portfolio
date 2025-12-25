from django.contrib import admin
from .models import Page, Post, TimeEntry, Entry

# Register your models here.
admin.site.register(Page)
admin.site.register(Entry)
admin.site.register(TimeEntry)
admin.site.register(Post)