from django import forms
from .models import Patient

class patientform(forms.ModelForm):
    class Meta:
        model = Patient

        fields = [
            "fname",
            "lname",
            "gender",
            "age"]