from django import forms
from django.conf import settings
from django.core.mail import send_mail

class ContactForm(forms.Form):
    your_name = forms.CharField()
    your_email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    
    def send_email(self):
        try:
            subject = self.cleaned_data.get('subject')
            message = self.cleaned_data.get('message')+"\n\n sender: " + self.cleaned_data.get('your_name') + "\n\n " + self.cleaned_data.get('your_email')
            from_address = settings.EMAIL_HOST_USER
        except Exception,e:
            print str(e)
        try:

            send_mail(subject, 
                      message,
                      from_address, 
                      ['leo.van.nierop@gmail.com'], 
                      fail_silently=False)
          
        except Exception, e:
            print str(e)
        