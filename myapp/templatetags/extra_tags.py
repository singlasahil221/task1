from django import template

register = template.Library()
@register.filter(name = "key")
def key(d, key_name):
	if(key_name not in d):
		return ''
	return d[key_name]