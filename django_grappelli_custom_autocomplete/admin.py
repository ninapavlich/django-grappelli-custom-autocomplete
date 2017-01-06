from django.contrib import admin

class CustomAutocompleteMixin(admin.ModelAdmin):
	change_form_template = 'admin/django_grappelli_custom_autocomplete/change_form.html'

	class Media:        
		css = {
			"all": ('django_grappelli_custom_autocomplete/css/django-grappelli-custom-autocomplete.css',)
		}
		js = [
			'django_grappelli_custom_autocomplete/js/jquery.grp_custom_autocomplete_fk.js',
			'django_grappelli_custom_autocomplete/js/jquery.grp_custom_autocomplete_generic.js',
			'django_grappelli_custom_autocomplete/js/jquery.grp_custom_autocomplete_m2m.js',
		]

