from django.contrib import admin
from portfolio.models import Board, MPTTComment
from mptt.admin import DraggableMPTTAdmin


# Register your models here.
@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('location', 'title', 'views', 'replies', 'name', 'date', 'created_at')

@admin.register(MPTTComment)
class MPTTCommentAdmin(admin.ModelAdmin):
    list_display = ('board', 'parent', 'author', 'comment', 'created_at')