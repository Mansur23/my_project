# from django.contrib import admin
# from . import models
# from mptt.admin import MPTTModelAdmin
#
# from .models import Category, Tag, Post, Recipe, Comment
#
# #
# # @admin.register(models.Post)
# # class PostAdmin(admin.ModelAdmin):
# #     list_display = ["title", "categore", "author", "create_at", "id"]
#
# #
# # @admin.register(models.Recipe)
# # class RecipeAdmin(admin.ModelAdmin):
# #     list_display = ["name", "prep_time", "cook_time", "post"]
#
#
# admin.site.register(Category, MPTTModelAdmin)
# admin.site.register(Tag)
# admin.site.register(Post)
# admin.site.register(Recipe)
# admin.site.register(Comment)

from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


class RecipeInline(admin.StackedInline):
    model = models.Recipe
    extra = 1


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "author", "create_at", "id"]
    prepopulated_fields = {'slug': ('title', 'category'), }
    inlines = [RecipeInline]
    save_as = True
    save_on_top = True


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name", "prep_time", "cook_time", "post"]


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'website', 'create_at', 'id']


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)