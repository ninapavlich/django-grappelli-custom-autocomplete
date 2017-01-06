django-grappelli-custom-autocomplete
=======================

This library gives you the ability to customize the display of the grappelli FK / M2M autocomplete lookup.

![Screenshot of custom lookup](/../master/docs/screenshots/screenshot.png?raw=true "Screenshot of custom lookup")

Requirements
=====
Requires Django and django-grappelli

Usage
=====
1. pip install django-grappelli-custom-autocomplete
2. Add 'django_grappelli_custom_autocomplete' to your INSTALLED_APPS list in your project's settings.py
3. Add to custom urls to urls.py: url(r'^grappelli_custom_autocomplete/', include('django_grappelli_custom_autocomplete.urls')),

```python
#admin.py
from django_grappelli_custom_autocomplete.admin import CustomAutocompleteMixin

class PageAdmin(CustomAutocompleteMixin, admin.ModelAdmin):
	
	fields = ['title', 'thumbnail']
	raw_id_fields = ['thumbnail']
	custom_autocomplete_lookup_fields = {
        'fk':['thumbnail'],
        'm2m': []
    }


#models.py
class Image( BaseImage ):

    """
    ...Your fields here...
    """
    
    def custom_related_dropdown_label(self):
        return "<img src='%s' width='150' /><br />%s" % (self.thumbnail.url, self.title)
    custom_related_dropdown_label.allow_tags = True

    def custom_related_selected_display(self):
        return "<img src='%s' width='150' />" % (self.thumbnail.url)
    custom_related_selected_display.allow_tags = True
```
