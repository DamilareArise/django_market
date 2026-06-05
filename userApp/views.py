from django.shortcuts import render
from django.views import generic
from .forms import SignupForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

class SignupView(generic.CreateView):
    form_class = SignupForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
    
    def post(self, request, *args, **kwargs):
        user_email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        try:
            send_mail(
                subject='Welcome to Django Market',
                message=f'Hello {first_name}! Thank you from joining Django Market. We hope you have a nice shopping experience.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user_email],
                fail_silently=False,  # Raise error if sending fails
            )
        except Exception as e:
            print("Error Sending mail:", e)
        
        return super().post(request, *args, **kwargs)
    