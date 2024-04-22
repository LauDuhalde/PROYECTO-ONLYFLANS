from django import forms
from .models import ContactForm

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email','customer_name','message']
        #labels = {
         #   'customer_email': 'Correo Electrónico',
          #  'customer_name': 'Nombre',
           # 'message': 'Mensaje'
            #}
#class ContactForm(forms.Form):
    #customer_email = forms.EmailField(label='Email')
    #customer_name = forms.CharField(label='Name', max_length=64)
    #message = forms.CharField(label='Message')