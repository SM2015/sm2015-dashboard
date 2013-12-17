from django import template
from tables import models
register = template.Library()

@register.tag
def table(model, *args, **kwargs):
    try:
        table_class = getattr(models, model)
        instances_list = table_class.objects.filter(**kwargs)
        if not instances_list:
            rendered = ""
        else:
            rendered = table_class.render_table(instances_list)

        return rendered
    except AttributeError, e:
        logging.error("[TABLE - TemplateTag] - Table Model not found >> ", e)
        return ""
