from django.views.generic import TemplateView
from typing import Dict
from ..moon_api import get_lunar_phase_service
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
User = get_user_model()

class LunarphaseView(LoginRequiredMixin, TemplateView):

    template_name = "lunarphase.html"

    def get_context_data(self, **kwargs) -> Dict:
        context_data = get_lunar_phase_service()
        context = {"lunar_image": context_data.get("data", {}).get("imageUrl")}
        return context