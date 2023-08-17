from django.contrib import admin
from .models import Adver


class AdverAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'title', 'discriptions', 'price', 'created_date', 'auction', 'updated_date', 'image',
    ]
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']

    fieldsets= (
        ('общее', {
            'fields' : ('title', 'discriptions', 'image')
        }),
        ('финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )

    @admin.action(description='убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)


admin.site.register(Adver, AdverAdmin)

