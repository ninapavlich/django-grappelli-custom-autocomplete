from django.contrib import admin


class CustomAutocompleteStackedMixin(admin.StackedInline):
	template = 'admin/django_grappelli_custom_autocomplete/edit_inline/stacked.html'

	class Media:        
		css = {
			"all": ('django_grappelli_custom_autocomplete/css/django-grappelli-custom-autocomplete.css',)
		}
		js = [
			'django_grappelli_custom_autocomplete/js/grp_custom_autocomplete_functions.js',
			'django_grappelli_custom_autocomplete/js/jquery.grp_custom_autocomplete_fk.js',
			'django_grappelli_custom_autocomplete/js/jquery.grp_custom_autocomplete_generic.js',
			'django_grappelli_custom_autocomplete/js/jquery.grp_custom_autocomplete_m2m.js',
		]


class CustomAutocompleteTabularMixin(admin.TabularInline):
	template = 'admin/django_grappelli_custom_autocomplete/edit_inline/tabular.html'

	class Media:        
		css = {
			"all": ('django_grappelli_custom_autocomplete/css/django-grappelli-custom-autocomplete.css',)
		}
		js = [
			'django_grappelli_custom_autocomplete/js/grp_custom_autocomplete_functions.js',
			'django_grappelli_custom_autocomplete/js/jquery.grp_custom_autocomplete_fk.js',
			'django_grappelli_custom_autocomplete/js/jquery.grp_custom_autocomplete_generic.js',
			'django_grappelli_custom_autocomplete/js/jquery.grp_custom_autocomplete_m2m.js',
		]

class CustomAutocompleteMixin(admin.ModelAdmin):
	change_form_template = 'admin/django_grappelli_custom_autocomplete/change_form.html'

	class Media:        
		css = {
			"all": ('django_grappelli_custom_autocomplete/css/django-grappelli-custom-autocomplete.css',)
		}
		js = [
			'django_grappelli_custom_autocomplete/js/grp_custom_autocomplete_functions.js',
			'django_grappelli_custom_autocomplete/js/jquery.grp_custom_autocomplete_fk.js',
			'django_grappelli_custom_autocomplete/js/jquery.grp_custom_autocomplete_generic.js',
			'django_grappelli_custom_autocomplete/js/jquery.grp_custom_autocomplete_m2m.js',
		]

