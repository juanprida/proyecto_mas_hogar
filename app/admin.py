from django.contrib import admin
from .models import Project, ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ("title",)  # Display fields in the project list


admin.site.register(Project, ProjectAdmin)
