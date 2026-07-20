from django.contrib import admin
from .models import Post, Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'status', 'created_date' ,'published_date']
    list_filter = ['title']
    search_fields = ('author',)
    ordering = ('created_date',)




class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)