from django.contrib import admin
from .models import Page, Post, TimeEntry, Entry, SiteContent

# Register your models here.
admin.site.register(Page)
admin.site.register(Entry)
admin.site.register(TimeEntry)
admin.site.register(Post)

@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteContent.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False