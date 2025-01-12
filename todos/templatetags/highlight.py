from django import template
import re

register = template.Library()

@register.filter
def highlight_query(value, query):
    if not query:
        return value

    pattern = re.escape(query)
    highlighted = re.sub(f"({pattern})", r"<strong>\1</strong>", value, flags=re.IGNORECASE)

    return highlighted
