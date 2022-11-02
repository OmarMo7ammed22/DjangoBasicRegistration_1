from django.shortcuts import render, redirect
from .forms import SignupForm

# Create your views here.
def user_dashboard(request):
    return render(request, 'accounts/dashboard.html', context= {})


def user_signup(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)

        if signup_form.is_valid():
            signup_form.save()
            return redirect('login')

    else:
        signup_form = SignupForm()

    return render(request, 'accounts/signup.html', context= {'signup_form': signup_form,})




