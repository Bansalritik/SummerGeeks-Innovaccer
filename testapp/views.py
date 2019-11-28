from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from .forms import SubmissionForm, DepartureForm
from .models import data
from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from smtplib import SMTPException

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)


# Create your views here
# Function performed as the app runs
def Course(request):
    if request.method == "POST":
        if 'exit1' in request.POST:
            departure_form = DepartureForm(request.POST)
            if departure_form.is_valid():
                visitoremails = departure_form.cleaned_data['hostemailcheck']
                if data.objects.filter(visitoremail=visitoremails, departed=False).exists():
                    a = data.objects.get(visitoremail=visitoremails, departed=False)
                    a.departed = True
                    a.visitordeparturetime = datetime.now()
                    a.save()
                    checkintime = a.visitorarrivaltime.strftime("%I:%M%p")
                    checkouttime = a.visitordeparturetime.strftime("%I:%M%p")

                    # Trying for an exception while Sending Mail
                    try:
                        send_mail(
                            'Check-Out Details',
                            'NAME: ' + a.visitorname + '\nPhone: ' + a.visitorphone + '\nHostname: ' + a.hostname +
                            '\nCheck-In Time: ' + checkintime + '\nCheckout Time: ' + checkouttime +
                            '\nAddress Visited: ' + a.addressvisited + "\n\nThanks for Visiting us!",
                            settings.EMAIL_HOST_USER,
                            [a.visitoremail],
                            fail_silently=False,
                        )
                    except SMTPException as e:
                        print('There was an error sending an email: ', e)

                    # Assigning context and rendering the View

                    success_msg = "Checked-Out Successfully!"
                    submission_form = SubmissionForm()
                    departure_form = DepartureForm()
                    context = {
                        'success': success_msg,
                        'submission_form': submission_form,
                        'departure_form': departure_form,
                    }
                    return render(request, 'home.html', context)

                # Rendering the View if any kind of error pops up while checking out
                else:
                    error_msg = "Either the person with the same E-Mail address has checked-out OR you might be " \
                                "entering a wrong E-Mail address! Please Enter Again."
                    submission_form = SubmissionForm()
                    departure_form = DepartureForm()
                    context = {
                        'error': error_msg,
                        'submission_form': submission_form,
                        'departure_form': departure_form,
                    }
                    return render(request, 'home.html', context)

        # For Submission Form
        elif 'submission' in request.POST:
            submission_form = SubmissionForm(request.POST)
            if submission_form.is_valid() and not data.objects.filter(visitoremail=submission_form.cleaned_data['visitoremail'], departed=False).exists():
                visitorname = submission_form.cleaned_data['visitorname']
                visitoremail = submission_form.cleaned_data['visitoremail'] 
                visitorphone = submission_form.cleaned_data['visitorphone']
                hostemail = submission_form.cleaned_data['hostemail']
                hostphone = str(submission_form.cleaned_data['hostphone'])
                checkintimme = datetime.now()
                checkintimme = checkintimme.strftime("%I:%M%p")

                # Using google API to send mail here
                send_mail(
                    'Check-In Details',
                    'NAME: ' + visitorname + '\nPhone: ' + visitorphone + '\nVisitor E-Mail: ' + visitoremail +
                    '\nCheck-In Time: ' + checkintimme,
                    settings.EMAIL_HOST_USER,
                    [hostemail],
                    fail_silently=False,
                )
                try:
                    message = client.messages \
                        .create(
                            body='NAME: ' + visitorname + '\nPhone: ' + visitorphone + '\nVisitor E-Mail: ' + visitoremail +'\nCheck-In Time: ' + checkintimme,
                            from_='+17154082006',
                            to='+91' + hostphone
                        )
                    print('success')
                except TwilioRestException:
                    print('fail')
                submission_form.save()
                success_msg = "Checked-In Successfully!"
                submission_form = SubmissionForm()
                departure_form = DepartureForm()
                context = {
                    'success': success_msg,
                    'submission_form': submission_form,
                    'departure_form': departure_form,
                }
                return render(request, 'home.html', context)

            # Rendering the View if any kind of error pops up while checking out
            else:
                error_msg = "Either the person with the same E-Mail address has checked-in OR you might be entering " \
                                "a wrong E-Mail address! Please Enter Again."
                submission_form = SubmissionForm()
                departure_form = DepartureForm()
                context = {
                    'error': error_msg,
                    'submission_form': submission_form,
                    'departure_form': departure_form,
                }
                return render(request, 'home.html', context)

    # For default, The rendered view
    submission_form = SubmissionForm()
    departure_form = DepartureForm()
    return render(request, 'home.html', {'submission_form': submission_form, 'departure_form': departure_form})
