# contact/views.py
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email (this will be printed in the console in this example)
            send_mail(
                f"New Contact Form Submission from {name}",
                message,
                email,
                ['recipient@example.com'],  # Replace with your email
            )

            return render(request, 'contact/success.html', {'name': name})
    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})
