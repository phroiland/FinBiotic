from django.contrib import admin

from .models import Fill, Order


class FillInline(admin.TabularInline):
    model = Fill
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['order_text']}),
        (None, {'fields': ['price']}),
        (None, {'fields': ['units']}),
        ('Date information', {'fields': ['time'], 'classes': ['collapse']}),
    ]
    inlines = [FillInline]
    list_display = ('order_text', 'time', 'created')
    list_filter = ['time']
    search_fields = ['order_text']


admin.site.register(Order, OrderAdmin)
