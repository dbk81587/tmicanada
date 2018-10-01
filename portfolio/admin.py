from django.contrib import admin
from portfolio.models import Board

# Register your models here.
@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('location', 'title', 'views', 'replies', 'name', 'date', 'created_at')