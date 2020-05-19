# Django Blog

A personal blog written in Python using the Django framework.

## Running Instructions
The requirements.txt file includes all the python packages needed to run this blog. There are a few extra unused packages that I couldn't distinguish from those being used by the python tracker.

To launch the server simply type, `python manage.py runserver`, when in the **django-blog** directory.

This application uses a pre-populated **SQLITE** database to display the functionality of the website.

Should you need to access the admin site, visit the [/admin](/admin) page, there is a pre-defined superuser
**username:** Admin
**password** Snowplowanalytics

To access the **client side** of the website the homepage is located at [/home](/home).

## Site Contents
- Blog Homepage
- Projects Page
- About Page
- Contact Page
- Contact Success Page
- Detail pages for blog and project posts

## Additional Information
The contact me form will send an email with the message contents, sender name and sender email to the email adress specified in `email_settings.py`. Although for the sake of demonstration I am using the Django email backend that prints the email to the console. Upon uncommenting `EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'` in the file `settings.py` and entering a valid gmail into `email_settings.py` this function as desired.