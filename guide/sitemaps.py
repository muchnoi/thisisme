from django.contrib.sitemaps import Sitemap
from .models import Reference

class ReferenceSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return [ el for el in Reference.objects.all() if el.upload ]
        
#    def lastmod(self, obj):
#        return obj.year
