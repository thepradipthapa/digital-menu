from django import forms

class QRCodeForm(forms.Form):
    vendor_name = forms.CharField(
        label='Vendor Name',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter vendor name'}
            )
        )
    url = forms.URLField(
        label='Menu URL',
        max_length=200,
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter menu URL'}
        )
    )