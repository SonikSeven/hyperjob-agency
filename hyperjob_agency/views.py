from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, redirect_to_login
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy


class HyperSignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login_url")
    template_name = "menu/signup.html"


class HyperLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "menu/login.html"


class Main(View):
    menu_links = {"Login page": reverse_lazy("login_url"),
                  "Logout page": reverse_lazy("logout_url"),
                  "Sign-up": reverse_lazy("signup_url"),
                  "Vacancy": reverse_lazy("vacancies_url"),
                  "Resume": reverse_lazy("resumes_url"),
                  "Personal profile": reverse_lazy("home_url")}

    def get(self, request):
        return render(request, "menu/main.html", context={"menu_links": self.menu_links})


class HomeView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            return redirect("new_vacancy_url")
        elif request.user.is_authenticated:
            return redirect("new_resume_url")
        else:
            return redirect_to_login("home_url")
