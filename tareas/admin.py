from django.contrib import admin
from .models import Tarea
# Register your models here.

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'completada', 'fecha_creacion')
    list_filter = ('completada', 'fecha_creacion')
    search_fields = ('titulo', 'descripcion')
    ordering = ('fecha_creacion',)
