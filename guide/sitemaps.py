from django.contrib.sitemaps import Sitemap
from .models import ReferenceType

class ItemsSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        print ('UUU', ReferenceType.objects.all())
        return ReferenceType.objects.all()
    
    def location(self, obj):
      return '/{:}'.format(obj.name)
        
#    def lastmod(self, obj):
#        return obj.year
