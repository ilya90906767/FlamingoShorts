from django.contrib import admin
from .models import LongVideo

class LongVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'uploaded_at', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'description')

admin.site.register(LongVideo, LongVideoAdmin)