# coding: utf-8

# DJANGO IMPORTS
from django.conf.urls import url
# from django.views.generic import TemplateView

# GRAPPELLI IMPORTS
from .views.related import CustomRelatedLookup, CustomM2MLookup, CustomAutocompleteLookup


urlpatterns = [

    # FOREIGNKEY & GENERIC LOOKUP
    url(r'^lookup/related/$', CustomRelatedLookup.as_view(), name="custom_related_lookup"),
    url(r'^lookup/m2m/$', CustomM2MLookup.as_view(), name="custom_m2m_lookup"),
    url(r'^lookup/autocomplete/$', CustomAutocompleteLookup.as_view(), name="custom_autocomplete_lookup"),

]
