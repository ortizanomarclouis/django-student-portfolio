from django.contrib import admin
from .models import Profile, Skill, Project, Education, Contact

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'location']
    # Remove 'avatar' from list_display if you don't want it shown in the list

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'percentage']
    list_filter = ['percentage']  # Fixed: removed 'level' which doesn't exist

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured']
    list_filter = ['featured']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['school', 'degree', 'start_date', 'end_date']
    list_filter = ['start_date', 'end_date']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    list_filter = ['created_at']
    readonly_fields = ['created_at']
    search_fields = ['name', 'email', 'subject']