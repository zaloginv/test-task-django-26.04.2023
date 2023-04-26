from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import ExtendedRegisterForm, BalanceReplenishmentForm
from .models import Profile


class RegisterView(CreateView):
    form_class = ExtendedRegisterForm
    template_name = 'app_users/register.html'
    success_url = reverse_lazy('app-users:profile')


    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)

        user = authenticate(
            self.request,
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password1'),
        )

        login(request=self.request, user=user)
        return response



class ProfileLoginView(LoginView):
    template_name = 'app_users/login.html'
    redirect_authenticated_user = True


class ProfileLogoutView(LogoutView):
    next_page = reverse_lazy('app-users:login')

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.success(request, 'You are successfully logged out.')
        return response


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'app_users/profile.html'


class BalanceReplenishment(LoginRequiredMixin, TemplateView):
    success_url = reverse_lazy('app-users:profile')
    template_name = 'app_users/balance_replenishment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BalanceReplenishmentForm()
        return context

    def post(self, request):
        profile = Profile.objects.get(user=self.request.user)
        form = BalanceReplenishmentForm(request.POST)
        if form.is_valid():
            profile.balance += form.cleaned_data['sum_to_replenishment']
            profile.save()
        return redirect('app-users:profile')