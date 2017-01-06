# coding: utf-8

# python imports
from functools import wraps
import json

try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User

# django imports
from django import template
from django.contrib.contenttypes.models import ContentType
from django.utils.formats import get_format
from django.utils.safestring import mark_safe
from django.utils.translation import get_language
from django.template.loader import get_template
from django.template.context import Context
from django.utils.translation import ugettext as _

# grappelli imports
from grappelli.settings import ADMIN_TITLE, ADMIN_URL, SWITCH_USER, SWITCH_USER_ORIGINAL, SWITCH_USER_TARGET, CLEAN_INPUT_TYPES
from grappelli.templatetags.grp_tags import safe_json_else_list_tag

register = template.Library()


# GENERIC OBJECTS
class do_get_generic_objects(template.Node):
    def __init__(self):
        pass

    def render(self, context):
        objects = {}
        for c in ContentType.objects.all().order_by('id'):
            objects[c.id] = {'pk': c.id, 'app': c.app_label, 'model': c.model}
        return json.dumps(objects)

# AUTOCOMPLETES

@register.assignment_tag()
def get_custom_autocomplete_lookup_fields_fk(model_admin):
    if getattr(model_admin, "custom_autocomplete_lookup_fields", None):
        return model_admin.custom_autocomplete_lookup_fields.get("fk", [])
    return []


@register.assignment_tag()
def get_custom_autocomplete_lookup_fields_m2m(model_admin):
    if getattr(model_admin, "custom_autocomplete_lookup_fields", None):
        return model_admin.custom_autocomplete_lookup_fields.get("m2m", [])
    return []


@register.assignment_tag()
def get_custom_autocomplete_lookup_fields_generic(model_admin):
    if getattr(model_admin, "custom_autocomplete_lookup_fields", None):
        return model_admin.custom_autocomplete_lookup_fields.get("generic", [])
    return []

