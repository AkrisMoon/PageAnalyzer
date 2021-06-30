from django.forms import ModelForm, CharField, TextInput, CheckboxInput
from djangoProject.models import Inquiry

class InquiryForm(ModelForm):
    class Meta:
        model = Inquiry
        fields = ['page']
