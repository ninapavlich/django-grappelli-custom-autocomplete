django-grappelli-custom-autocomplete
=======================

This library gives you the ability to customize the display of the grappelli FK / M2M autocomplete lookup.

![Screenshot of custom FK lookup](/../master/docs/screenshots/fk_selection.png?raw=true "Screenshot of custom FK lookup")
![Screenshot of custom M2M lookup](/../master/docs/screenshots/m2m_selection.png?raw=true "Screenshot of custom M2M lookup")
![Better M2M delete display](/../master/docs/screenshots/delete_ux.png?raw=true "Screenshot of M2M delete")

Requirements
=====
Requires Django and django-grappelli

Installation
=====
1. pip install django-grappelli-custom-autocomplete
2. Add 'django_grappelli_custom_autocomplete' to your INSTALLED_APPS list in your project's settings.py
3. Add to custom urls to urls.py: url(r'^grappelli_custom_autocomplete/', include('django_grappelli_custom_autocomplete.urls')),

Usage
=====
```python
#admin.py
from django_grappelli_custom_autocomplete.admin import CustomAutocompleteMixin

class PageAdmin(CustomAutocompleteMixin, admin.ModelAdmin):
	
	fields = ['title', 'thumbnail', 'slides']
	raw_id_fields = ['thumbnail', 'slides']
	custom_autocomplete_lookup_fields = {
        'fk':['thumbnail'],
        'm2m': ['slides']
    }


#models.py
class Image( BaseImage ):

    """
    ...Your fields here...
    """
    

    """
    Define the following three functions on the model to return custom 
    autocomplete markup:
    """
    def custom_related_dropdown_label(self):
        #This is the HTML that gets used in the dropdown selector.
        return "%s<br /><img src='%s' width='100' />" % (self.title, self.thumbnail.url)
    

    def custom_related_fk_selected_display(self):
        #This is the HTML that gets inserted next to the FK selector to 
        return "<img src='%s' width='100' />" % (self.thumbnail.url)
   
    def custom_related_m2m_selected_display(self):
        #This is the HTML that gets used in the M2M list
        return "<img src='%s' height='35' /> %s " % (self.thumbnail.url, self.title)
```
