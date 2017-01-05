from django.contrib import admin

class AdminListOrderable(admin.ModelAdmin):
	change_list_template = 'admin/django_grappelli_custom_autocomplete/change_list.html'

	def changelist_view(self, request, extra_context=None):
		extra_context = extra_context or {}
		extra_context['ORDER_BY'] = self.custom_list_order_by or 'order'
		return super(AdminListOrderable, self).changelist_view(request, extra_context=extra_context)
	class Media:        
		css = {
			"all": ('django_grappelli_custom_autocomplete/css/django-grappelli-custom-autocomplete.css',)
		}
		js = [
			'django_grappelli_custom_autocomplete/js/django-grappelli-custom-autocomplete.js' 
		]

