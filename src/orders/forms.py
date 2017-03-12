from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

from orders.models import UserAddress


class GuestCheckoutForm(forms.Form):
    email = forms.EmailField()
    email2 = forms.EmailField(label='confirm email')

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email == email2:
            is_user_exists = User.objects.filter(email=email).exists()
            if is_user_exists:
                raise forms.ValidationError(
                    'User already exists. Please login instead')
            return True
        else:
            raise forms.ValidationError('please confirm email')


class AddressForm(forms.Form):
    billing_address = forms.ModelChoiceField(queryset=UserAddress.objects.filter(type=UserAddress.BILLING),
                                             empty_label=None, widget=forms.RadioSelect)
    shipping_address = forms.ModelChoiceField(queryset=UserAddress.objects.filter(type=UserAddress.SHIPPING),
    										 empty_label=None, widget=forms.RadioSelect)


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ('type', 'address', 'state', 'zipcode')
