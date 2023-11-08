from django.contrib import admin
from .models import Posts


def make_publish(modeladmin, request, queryset):
    queryset.update(is_publish = True)
    
def make_unpublish(modeladmin, request, queryset):
    queryset.update(is_publish = False)


class PostsAdmin(admin.ModelAdmin):
    list_display = ['title','author', 'created','updated','is_publish','image']
    list_filter = ['author']
    search_fields = ['title', 'author__username', 'author__email', 'text']
    prepopulated_fields = {'slug':['title']}
    ordering = ['-created','title']
    actions = [make_publish, make_unpublish]

admin.site.register(Posts, PostsAdmin)

