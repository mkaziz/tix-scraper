from django.conf.urls import patterns, url
from django.conf import settings
from scraper.views import *

from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', index),
) + static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)

