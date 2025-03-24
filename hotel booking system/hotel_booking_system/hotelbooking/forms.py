# main/forms.py

from django import forms

class BookingForm(forms.Form):
    arrival = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Arrival Date'
    )
    departure = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Departure Date'
    )
    guests = forms.IntegerField(
        min_value=1,
        label='Number of Guests'
    )

    def clean(self):
        cleaned_data = super().clean()
        arrival = cleaned_data.get('arrival')
        departure = cleaned_data.get('departure')

        if arrival and departure:
            if departure <= arrival:
                raise forms.ValidationError("Departure date must be after arrival date.")
