from django.contrib import admin
from .models import FooterLinkModel, FooterLinkBoxModel, SliderModel


@admin.register(FooterLinkBoxModel)
class FooterLinkBoxAdmin(admin.ModelAdmin):
    list_display = ['title', 'active']
    list_filter = ['title']
    search_fields = ['title']
    list_editable = ['active']


@admin.register(FooterLinkModel)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['footer_link_box', 'title', 'url']
    list_filter = ['title']
    search_fields = ['title']
    raw_id_fields = ['footer_link_box']


@admin.register(SliderModel)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'active']
    list_filter = ['active']
    search_fields = ['title']
    list_editable = ['active']
