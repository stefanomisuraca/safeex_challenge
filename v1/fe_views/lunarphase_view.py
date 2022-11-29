from django.views.generic import TemplateView

from django.contrib.auth import get_user_model
User = get_user_model()

class LunarphaseView(TemplateView):

    template_name = "lunarphase.html"

    def get_context_data(self, **kwargs):
        context = {"data": "belli dati"}
        return context