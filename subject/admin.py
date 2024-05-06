from django.contrib import admin
from .models import Subject

# Register your models here.


@admin.register(Subject)
class Subject_Admin_Panel(admin.ModelAdmin):
    list_display = ['id', 'title', 'hashtag', 'author']
    list_display_links = ['title']
    readonly_fields = ('created_date', 'updated_date')
