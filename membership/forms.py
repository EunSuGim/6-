from django import forms
from membership.models import Gift_card

class Gift_cardForm(forms.ModelForm):
    class Meta :
        model = Gift_card
        fields = ['serial_number']