from django.shortcuts import render
from django.views.generic.base import TemplateView

from apps.user.admin import User

class UserView(TemplateView):
    template_name = "user/user-test.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Users'
        context['users'] = User.objects.all()
        return context