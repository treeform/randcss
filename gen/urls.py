from django.conf.urls.defaults import *


urlpatterns = patterns('randcss.gen.views',
    (r'^$', 'index'),
    (r'^design.html$', 'design'),
    (r'^style.css$', 'style'),
)
