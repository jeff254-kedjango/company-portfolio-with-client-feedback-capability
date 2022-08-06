from django.contrib import admin
from . import models


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
        'published',
    ]
    list_display_links = [
        'title',
    ]
    list_filter = [
        'category',
    ]
    search_fields = [
        'title',
        'category',
        'published',
    ]


class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
        'published',

    ]
    list_display_links = [
        'title',
    ]
    list_filter = [
        'category',
    ]
    search_fields = [
        'title',
        'category',
        'published',
    ]


class NutritionAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
        'published',

    ]
    list_display_links = [
        'title',
    ]
    list_filter = [
        'category',
    ]
    search_fields = [
        'title',
        'category',
        'published',
    ]


class FeedBackAdmin(admin.ModelAdmin):
    list_display = [
        'firstname',
        'lastname',
        'email',
    ]
    list_display_links = [
        'firstname',
    ]
    list_filter = [
        'published',
    ]
    search_fields = [
        'firstname',
        'lastname',
        'email',
    ]


admin.site.register(models.Projects, ProjectAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Feedback, FeedBackAdmin)
admin.site.register(models.Nutrition, NutritionAdmin)
admin.site.register(models.Category)
admin.site.register(models.ProjectCategory)
admin.site.register(models.NutritionCategory)
