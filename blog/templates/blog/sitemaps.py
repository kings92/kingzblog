from django.contrib.sitemaps import sitemap
from .models import Post 

class Postsitemap(Sitemap):
  changefreq = 'weekly'
  priority =0.9

  def items(self):
    return Post.published.all()


  def lastmod(self, obj):
    return obj.updated