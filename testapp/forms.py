from django import forms
from .models import data


# Form for submitting Visitor's Details
class SubmissionForm(forms.ModelForm):
    class Meta:
        model = data
        fields = ('visitorname', 'visitoremail', 'visitorphone', 'hostname', 'hostemail', 'hostphone')
        widgets = {
            'visitorname': forms.TextInput(
                attrs={'class': 'input', 'placeholder': "Visitor's Name", 'required': 'True'}),
            'visitoremail': forms.EmailInput(
                attrs={'class': 'input', 'placeholder': "Visitor's E-Mail", 'required': 'True'}),
            'visitorphone': forms.TextInput(
                attrs={'class': 'input', 'placeholder': "Visitor's Phone No.", 'required': 'True'}),
            'hostname': forms.TextInput(attrs={'class': 'input', 'placeholder': "Host's Name", 'required': 'True'}),
            'hostemail': forms.EmailInput(attrs={'class': 'input', 'placeholder': "Host's E-Mail", 'required': 'True'}),
            'hostphone': forms.TextInput(
                attrs={'class': 'input', 'placeholder': "Host's Phone No.", 'required': 'True'}),

        }


# Form for check-out details
class DepartureForm(forms.Form):
    hostemailcheck = forms.EmailField(label='',
                                      widget=forms.EmailInput(
                                          attrs={'placeholder': "Visitor's E-Mail", 'required': 'True'})
                                      )
