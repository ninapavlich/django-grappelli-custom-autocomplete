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
2. Add 'django-grappelli-custom-autocomplete' to your INSTALLED_APPS list in your project's settings.py

```python
from django-grappelli-custom-autocomplete.admin import TabularInlineOrderable, AdminListOrderable

from .models import *

class ObjectAdmin(CustomAutocompleteAdminMixin, admin.ModelAdmin):
	
	#TODO
```
