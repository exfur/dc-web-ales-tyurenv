from django.contrib import admin
from quality_control.models import BugReport, FeatureRequest


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'created_at', 'updated_at')
    search_fields = ('title', 'description')

    fieldsets = (
        ('Описание бага', {
            'fields': ('title', 'description')
        }),
        ('Связанные объекты', {
            'fields': ('project', 'task')
        }),
        ('Статус и приоритет', {
            'fields': ('status', 'priority')
        }),
        
    )

    actions = ['change_status_to_in_progress', 'change_status_to_completed']

    def change_status_to_in_progress(self, request, queryset):
        queryset.update(status='В работе')
    change_status_to_in_progress.short_description = "Изменить статус на 'В работе'"

    def change_status_to_completed(self, request, queryset):
        queryset.update(status='Завершена')
    change_status_to_completed.short_description = "Изменить статус на 'Завершена'"


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'created_at', 'updated_at')
    search_fields = ('title', 'description')

    fieldsets = (
        ('Описание запроса на новую функцию', {
            'fields': ('title', 'description')
        }),
        ('Связанные объекты', {
            'fields': ('project', 'task')
        }),
        ('Статус и приоритет', {
            'fields': ('status', 'priority')
        }),
       
    )
    

