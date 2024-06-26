from django.core.cache import cache
from django.shortcuts import render
from apps.site_setting.models import FooterLinkBoxModel


def header_component(request):
    context = {}
    return render(request, 'utils/header.html', context)


def footer_component(request):
    footer_link_boxes = cache.get('footer')
    if not footer_link_boxes:
        footer_link_boxes = FooterLinkBoxModel.objects.filter(active=True)[:3]
        cache.set('footer', footer_link_boxes, 60 * 2)
    context = {
        'footer_link_boxes': footer_link_boxes,
    }
    return render(request, 'utils/footer.html', context)
