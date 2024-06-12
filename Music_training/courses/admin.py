from django.contrib import admin
from .models import Subject, Course, Module

@admin.register(Subject) # декоратор, чтобы зарегистрировать модель на сайте администрирования
class SubjectAdmin(admin.ModelAdmin): # page 305
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

class ModuleInline(admin.StackedInline): # page 305
    model = Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin): # page 305
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]

