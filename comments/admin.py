from django.contrib import admin
from .models import Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url']

admin.site.register(Comment,PostAdmin)
# Register your models here.
