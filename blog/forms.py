from django import forms
from django.core.mail import send_mail
from blogsite.email_settings import *

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        sender_name = self.cleaned_data['name']
        sender_email = self.cleaned_data['email']

        message = "{0} has sent you a new message:\n\n{1}\n\nContact Email: {2}".format(sender_name, self.cleaned_data['message'], self.cleaned_data['email'])
        send_mail('New Enquiry', message, sender_email, [EMAIL_HOST_USER], fail_silently=False)