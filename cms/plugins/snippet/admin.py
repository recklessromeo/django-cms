from models import Snippet
from django.contrib import admin

class SnippetAdmin(admin.ModelAdmin):

    def duplicate_event(modeladmin, request, queryset):
        for object in queryset:
            object.id = None
            object.name = object.name + "-copy"
            object.save()
    duplicate_event.short_description = "Duplicate selected record"

    actions = ['duplicate_event']

admin.site.register(Snippet, SnippetAdmin)
