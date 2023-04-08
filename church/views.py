from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print("name", name)
        email = request.POST.get('email')
        print("email", email)
        subject = request.POST.get('subject')
        print("subject", subject)
        message = request.POST.get('message')
        print("message", message)

        # sending email
        send_mail(
            subject,
            f"Name: {name}\nEmail: {email}\n\n{message}",
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        # Send text message
        # url = "https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json".format(account_sid=settings.TWILIO_ACCOUNT_SID)
        # data = {
        #     "From": settings.TWILIO_PHONE_NUMBER,
        #     "To": settings.MY_PHONE_NUMBER,
        #     "Body": f"Name: {name}\nEmail: {email}\n\n{message}"
        # }
        # auth = (settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        # response = requests.post(url, data=data, auth=auth)
        return render(request, 'success.html')
    return render(request, 'contact.html')


def declaration(request):
    return render(request, 'declaration.html')
