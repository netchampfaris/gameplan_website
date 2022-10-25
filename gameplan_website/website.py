# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import os
import frappe
from frappe.utils.jinja_globals import resolve_class


def website_context(context):
    context.x = get_components()

def get_components():
    if hasattr(frappe.local, 'website_components'):
        return frappe.local.website_components

    out = {}
    def get_renderers(path):
        renderers = {}
        for file in os.listdir(path):
            filepath = os.path.join(path, file)
            relpath = os.path.relpath(filepath, frappe.get_app_path('gameplan_website'))
            if file.endswith(".html"):
                renderers[file[:-5]] = get_renderer(relpath)
        return renderers

    components_path = frappe.get_app_path('gameplan_website', 'templates', 'components')
    for dirpath, dirnames, filenames in os.walk(components_path):
        relative_path = os.path.relpath(dirpath, components_path)
        if relative_path == '.':
            curr_obj = out
        else:
            curr_obj = out
            for part in relative_path.split(os.path.sep):
                curr_obj = curr_obj.setdefault(part, {})
        curr_obj.update(get_renderers(dirpath))

    frappe.local.website_components = out
    return out

def get_renderer(file):
    if not file.endswith(".html"):
        file = file + ".html"

    def render(**context):
        def resolve_attrs(keys=None):
            attrs = {}
            for key, value in context.items():
                if key in ['resolve_attrs', 'x']: continue
                if keys and key not in keys: continue
                attrs[key] = value
                if key == 'class':
                    attrs['class'] = resolve_class(value)
            return ' '.join(f'{key}="{value}"' for key, value in attrs.items())

        context['resolve_attrs'] = resolve_attrs
        context['x'] = get_components()
        return frappe.render_template(file, context=context or {})

    return render

