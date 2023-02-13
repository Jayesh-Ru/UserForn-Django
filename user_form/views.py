from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import RegistrationForm
from .models import UserDetails
from django.http.response import JsonResponse

# Create your views here.


def UserForm(request):
    print('hello')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.phone = registerForm.cleaned_data['phonenumber']

            user.save()
            subject = 'Confirmation Email'
            message = render_to_string('user_confirmation_email.html', {
                'user': user,
            })
            user.email_user(subject=subject, message=message)
            return redirect('user_form:user_all')
    else:
        registerForm = RegistrationForm()
    return render(request, 'index.html', {'form': registerForm})


def User_all(request):
    users = UserDetails.objects.all()
    return render(request, 'user_details.html', {'user': users})
