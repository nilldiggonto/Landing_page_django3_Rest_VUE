from django.conf import settings

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class IndexTemplateView(LoginRequiredMixin,TemplateView):
    def get_template_names(self):
        if not settings.DEBUG:
            template_name = 'index.html'
        else:
            template_name= 'main.html'
        return template_name