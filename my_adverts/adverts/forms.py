from django import forms


class AdvertForm(forms.Form):
    title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class' : 'form-control-lg'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control-lg'}))
    photo = forms.ImageField(widget=forms.FileInput(attrs={'class' : 'form-control-lg'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class' : 'form-control-lg'}))
    auction = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class' : 'form-check-input'}))
    category = forms.DecimalField(widget=forms.NumberInput(attrs={'class' : 'form-control-lg'}))
    isActual = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class' : 'form-check-input'}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class' : 'form-control-lg'}))

