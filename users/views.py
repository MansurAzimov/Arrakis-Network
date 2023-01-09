from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import RegisterForm


class SignUpView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
