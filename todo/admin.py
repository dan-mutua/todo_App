from django.contrib import admin
from .models import  Todo

# Register your models here.
@admin.register(Todo)
class Todo(admin.ModelAdmin):
    list_display=['title','complete','created_at']
    list_filter=['complete', 'created_at']
    readonly_fields=['created_at']
