from django import forms
from .models import Disease, AGE_GROUPS

class PatientEntryForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for disease in Disease.objects.all():
            for age_code, age_label in AGE_GROUPS:
                self.fields[f"{disease.name}_{age_code}_male"] = forms.IntegerField(
                    min_value=0, label=f"{disease.name} ({age_label}) - Male", required=False
                )
                self.fields[f"{disease.name}_{age_code}_female"] = forms.IntegerField(
                    min_value=0, label=f"{disease.name} ({age_label}) - Female", required=False
                )
